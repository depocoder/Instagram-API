import os
from pathlib import Path
import requests


def parse_links():
    url = 'https://api.spacexdata.com/v4/launches/latest'
    response = requests.get(url)
    return response.json()['links']["flickr"]['original']


def download_img(num_pic, link):
    response = requests.get(link)
    folder = os.path.join(os.getcwd(), 'images', f"spacex{num_pic}.jpg")
    with open(folder, 'wb') as file:
        return file.write(response.content)


if __name__ == "__main__":
    base_url = 'https://api.spacexdata.com/v3'
    Path(os.getcwd(), 'images').mkdir(parents=True, exist_ok=True)
    for num_pic, link in enumerate(parse_links(), 1):
        download_img(num_pic, link)
