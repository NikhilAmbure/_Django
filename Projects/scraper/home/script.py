import requests
from bs4 import BeautifulSoup
from .models import News
import os
import uuid

# Downloading images locally
def download_image(image_url, save_directory, image_name):
    if os.path.exists(save_directory):
        os.makedirs(save_directory)
    image_path = os.path.join(save_directory, image_name)

    # To download image use stream = True
    response = requests.get(image_url, stream=True)

    if response.status_code == 200:
        with open(image_name, 'wb') as file:
            # 1024 is chunk size
            for chunk in response.iter_content(1024):
                file.write(chunk)

    return image_url


def scrap_news():
    url = "https://www.imdb.com/news/movie/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    }

    response = requests.get(url, headers=headers)
    
    # soup sets the html in tree format
    soup = BeautifulSoup(response.text, 'html.parser')

    news_items = soup.find_all('div', class_="ipc-list-card--border-line")

    for item in news_items:
        title = item.find('a', class_="ipc-link ipc-link--base sc-781c1bad-2 jZxGAW")
        desc = item.find('div', class_= "ipc-html-content-inner-div")
        image = item.find('img', class_="ipc-image")

        external_link = title['href']

        title = title.text.strip() if title else "No Title"
        desc = desc.text.strip() if title else "No desc"
        image = image['src']

        image_path = None

        if image:
            image_name = f"image_{uuid.uuid4()}.jpg"
            image_path = download_image(image, 'downloads', image_name)
        
        news = {
            "title": title,
            "desc": desc,
            "image": image,
            "external_link": external_link,
        }

        News.objects.create(**news)
    
