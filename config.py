import yaml

with open('config.yaml', mode='r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

username = config['username']
password = config['password']
download_dir = config['download_dir']
proxies = config['proxies']
repository = config['repository']

__all__ = [
    "username",
    "password",
    "download_dir",
    "proxies",
    "repository",
]
