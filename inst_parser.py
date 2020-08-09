import os
from pathlib import Path
import requests


url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
response = requests.get(url)
Path(os.getcwd(), 'images').mkdir(parents=True, exist_ok=True)
folder = os.path.join(os.getcwd(), 'images', 'filename.jpeg')
with open(folder, 'wb') as file:
    file.write(response.content)

