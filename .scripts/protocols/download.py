import json
import os
import requests
import shutil
import sys
import urllib.parse
from zipfile import ZipFile

def fix_dropbox(url):
    if url.startswith("https://www.dropbox.com/"):
        url = url.replace("?dl=0","?dl=1")
        if not url.endswith("?dl=1"):
            url = url.split("?")[0]+"?dl=1"
    return url

def download_zipped_folder(folder_url, dest):
    # download whole dropbox folder as zip file
    folder_url = fix_dropbox(folder_url)
    r = requests.get(folder_url, stream=True)
    zf = os.path.join(dest,"temp.zip")
    with open(zf, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk:
                f.write(chunk)
    with ZipFile(zf, 'r') as zipObj:
        zipObj.extractall(dest)

with open("settings.json") as fp:
    config = json.load(fp)

location = list(config.keys())[0]
config = config[location]

scriptpath = os.path.dirname(os.path.realpath(__file__))

for subdir in config["sources"]:
    dir = os.path.join(scriptpath, config['download_dir'], subdir[0])
    if os.path.exists(dir):
        shutil.rmtree(dir)
    os.mkdir(dir)
    print (dir, subdir[1])
    download_zipped_folder(subdir[1], os.path.abspath(dir))
