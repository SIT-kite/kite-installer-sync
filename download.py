import os.path

import requests
from config import proxies, repository, download_dir

session = requests.Session()
session.proxies = proxies

assets = session.get(f'https://api.github.com/repos/{repository}/releases/latest').json()['assets']

assets_dict = {}

assets_output_paths = []

for asset in assets:
    name = asset['name']
    url = asset['browser_download_url']
    assets_dict[name] = url

for i, (name, url) in enumerate(assets_dict.items()):
    output_path = os.path.abspath(download_dir)+f'/{name}'
    print(f'正在下载({i+1}/{len(assets_dict)})：{output_path}')
    if os.path.exists(output_path):
        assets_output_paths.append(output_path)
        continue
    with open(output_path, 'wb') as f:
        bs = session.get(url).content
        f.write(bs)
        assets_output_paths.append(output_path)

__all__ = ['assets_output_paths']

