# requests-bs4-article

The script’s purpose is to automate system-oriented tasks related to retrieving data from Wikipedia.
It specifically focuses on extracting the content of the “Artykuł na medal” (Featured Article) along with associated images.

The script follows these steps:

Retrieves the HTML content of the Wikipedia homepage.
Identifies the link to the “Artykuł na medal” using a CSS selector.
Fetches the content of the featured article by following the identified link.
Removes any tables from the article content.
Extracts the text paragraphs from the article.
Cleans the text by removing HTML tags.
Saves the cleaned article text to a text file named “artykul_na_medal.txt”.
Collects image URLs from the article.
Downloads the images and saves them in a folder named “images”.


Key Components:
- Web Scraping:
The script uses the requests library to fetch web pages.
It utilizes BeautifulSoup for parsing HTML content and extracting relevant data.
- Article Text Extraction:
The article text is extracted from the HTML content using a CSS selector.
Tables are removed to improve readability.
The cleaned text is saved to a text file.
- Image Handling:
Image URLs are collected from the article.
Images are downloaded and saved in the “images” folder.
- Output:
The script generates two outputs:
A text file (“artykul_na_medal.txt”) containing the cleaned article text.
A folder (“images”) with downloaded images related to the article.


Overall, the script automates the process of fetching and processing Wikipedia content, making it more understandable and maintainable.
