import os
from pathlib import Path
import requests


def download_img():
    url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    response = requests.get(url)
    folder = os.path.join(os.getcwd(), 'images', 'filename.jpeg')
    with open(folder, 'wb') as file:
        return file.write(response.content)


if __name__ == "__main__":
    Path(os.getcwd(), 'images').mkdir(parents=True, exist_ok=True)
    download_img()


