import os
from pathlib import Path
from random import choice
from urllib.parse import urljoin
import requests


def parse_ids():
    url = 'http://hubblesite.org/api/v3/images/wallpaper'
    response = requests.get(url)
    response.raise_for_status()
    ids = []
    for id in response.json():
        ids.append(id['id']) 
    return ids


def parse_link_hubble(id):
    url = f'http://hubblesite.org/api/v3/image/{id}'
    response = requests.get(url)
    response.raise_for_status()
    links = response.json()["image_files"]
    link = choice(links)['file_url'].split(
        'imgsrc.hubblesite.org/hvi/uploads/')
    return urljoin('https://media.stsci.edu/uploads/', link[1])
     

def download_content(link, id):
    response = requests.get(link)
    response.raise_for_status()
    filename_extension = link.split('.')[-1]
    folder = os.path.join(os.getcwd(), 'images', f"{id}.{filename_extension}")
    with open(folder, 'wb') as file:
        return file.write(response.content)


if __name__ == "__main__":
    Path(os.getcwd(), 'images').mkdir(parents=True, exist_ok=True)
    #for num_pic, link in enumerate(parse_links(), 1):
        #fetch_spacex_last_launch(num_pic, link)
    ids = parse_ids()
    for id in ids:
        link = parse_link_hubble(id)
        download_content(link, id)
