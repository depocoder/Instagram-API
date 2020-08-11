import os
from pathlib import Path
from urllib.parse import urljoin
import requests


def parse_ids():
    url = 'http://hubblesite.org/api/v3/images/wallpaper'
    response = requests.get(url)
    response.raise_for_status()
    ids = [id['id'] for id in response.json()]
    return ids


def parse_link_hubble(id):
    url = f'http://hubblesite.org/api/v3/image/{id}'
    response = requests.get(url)
    response.raise_for_status()
    links = response.json()["image_files"]
    return links


def choice_better_img(links):
    max = 0
    for num_link, link in enumerate(links):
        filename_extension = link['file_url'].split('.')[-1]
        if link['file_size'] > max and (
                filename_extension == 'jpg' or filename_extension == 'png'):
            max = link['file_size']
            max_num = num_link
    link = links[max_num]['file_url'].split(
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
    ids = parse_ids()
    for id in ids:
        links = parse_link_hubble(id)
        link = choice_better_img(links)
        download_content(link, id)
