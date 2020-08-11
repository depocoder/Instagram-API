import os
from pathlib import Path
import argparse
import shutil
from io import open
from urllib.parse import urljoin
import requests
from PIL import Image
from instabot import Bot


def parse_ids():
    url = 'http://hubblesite.org/api/v3/images/spacecraft'
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


def calculate_the_size(width, height):
    if (width / height) < (4 / 3):
        width = (width // 4) * 4
        height = (width // 4) * 3
    else:
        height = (height // 3) * 3
        width = (height // 3) * 4
    return width, height


def upload_photo(id, filename_extension):
    image = Image.open(f"images/{id}.{filename_extension}")
    image.thumbnail((1080, 1080))
    if image.format == 'PNG':
        image = image.convert("RGB")
        path = os.path.join(os.getcwd(), 'images', f'{id}.png')
        os.remove(path)
    crop_width, crop_height = calculate_the_size(
        image.width, image.height)
    coordinates = (
        image.width - crop_width, image.height - crop_height,
        image.width, image.height)
    image = image.crop(coordinates)
    image.save(f"images/{id}.jpg")
    return bot.upload_photo(
        os.path.join(os.getcwd(), 'images', f'{id}.jpg'), caption="Nice pic!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--username', nargs='?',
                        help='')
    parser.add_argument('--password', nargs='?',
                        help='')

    args = parser.parse_args()
    bot = Bot()
    bot.login(username=args.username, password=args.password)
    Path(os.getcwd(), 'images').mkdir(parents=True, exist_ok=True)
    ids = parse_ids()
    for id in ids:
        links = parse_link_hubble(id)
        link = choice_better_img(links)
        filename_extension = link.split('.')[-1]
        download_content(link, id)
        upload_photo(id, filename_extension)
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'images')
    shutil.rmtree(path)
