""""""

"""
Zadanie domowe
Napisz skrypt w języku Python, który po uruchomieniu otworzy stronę główną Wikipedii. 
Następnie pobierze treść "Artykułu na medal" wraz z wszystkimi obrazami z tej strony. 
Tekst artykułu powinien być oczyszczony z tagów HTML i zapisany do pliku tekstowego.
Obrazki powinny być zapisane w folderze images.
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
from requests import HTTPError


URL = "https://pl.wikipedia.org"
CSS_SELECTOR_LINK = "#main-page-featured-article > p > i:nth-child(11) > a"
CSS_SELECTOR_DATA = "#mw-content-text > div.mw-content-ltr.mw-parser-output"


def get_response():
    response = requests.get(URL)
    response.raise_for_status()
    return response.text


def get_article_link(response):
    soup = BeautifulSoup(response, 'html.parser')
    css_selector = CSS_SELECTOR_LINK
    article_title = soup.select(css_selector)

    if article_title:
        article_link = article_title[0].get('href')
        return article_link
    else:
        raise


def get_article_data(article_link):
    response = requests.get(urljoin(URL, article_link))
    soup = BeautifulSoup(response.text, 'html.parser')

    tab_all = soup.find_all('table')
    [tab.decompose() for tab in tab_all]

    css_selector = CSS_SELECTOR_DATA
    article = soup.select(css_selector)

    if article:
        for element in article:
            element = element.find_all('p')
            if element:
                for paragraph in element:
                    article_txt = paragraph.text
                    yield article_txt


def save_article_data(article_txt):
    for text in article_txt:
        with open("artykul_na_medal.txt", "a", encoding="utf-8") as file:
            file.write(text)
    print('[INFO-MESS] Pomyślnie zapisano tekst artykułu na medal!')


def get_img_data(response):
    soup = BeautifulSoup(response, 'html.parser')
    image_elements = soup.find_all("img")
    images_url = []
    for i, image_element in enumerate(image_elements):
        image_url = image_element["src"]

        if image_url.startswith('/static'):
            images_url.append(urljoin(URL, image_url))
        elif image_url.startswith('//upload'):
            images_url.append(urljoin('https:', image_url))
    return images_url


def save_img_data(image_url):
    for img in image_url:
        response = requests.get(img)
        try:
            if response.status_code == 200:
                img_file_name = os.path.basename(img)
                path_to_save = os.path.join('images', img_file_name)

                with open(path_to_save, "wb") as plik:
                    plik.write(response.content)
                print(f"Obrazek został zapisany jako: {path_to_save}")
        except Exception as error:
            print(f"Nie udało się pobrać obrazka: {error}")


def main():
    response = get_response()
    main_website = get_article_link(response)
    article_data = get_article_data(main_website)
    save_article_data(article_data)
    img_data = get_img_data(response)
    save_img_data(img_data)


if __name__ == '__main__':
    main()
