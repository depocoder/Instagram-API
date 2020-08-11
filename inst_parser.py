import os
from pathlib import Path
from urllib.parse import urljoin
import requests


def parse_links():
    url = 'https://api.spacexdata.com/v4/launches/latest'
    response = requests.get(url)
    return response.json()['links']["flickr"]['original']


def parse_links_hubble():
    url = 'http://hubblesite.org/api/v3/image/1'
    response = requests.get(url)
    return response.json()["image_files"]


def fetch_spacex_last_launch(num_pic, link):
    response = requests.get(link)
    folder = os.path.join(os.getcwd(), 'images', f"spacex{num_pic}.jpg")
    with open(folder, 'wb') as file:
        return file.write(response.content)


if __name__ == "__main__":
    base_url = 'https://api.spacexdata.com/v3'
    Path(os.getcwd(), 'images').mkdir(parents=True, exist_ok=True)
    for num_pic, link in enumerate(parse_links(), 1):
        fetch_spacex_last_launch(num_pic, link)
    for link in parse_links_hubble():
        link = link['file_url'].split('imgsrc.hubblesite.org/hvi/uploads/')
        print(urljoin('https://media.stsci.edu/uploads/', link[1]))
