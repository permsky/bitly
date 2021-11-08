import argparse
import os

from urllib.parse import urlparse

import requests
from dotenv import load_dotenv


def get_url() -> str:
    """Return the URL entered as an argument."""
    parser = argparse.ArgumentParser(
        description='Скрипт для преобразования длинной ссылки в битлинк вида '
        'bit.ly/1ABCdef. В случае ввода вашего битлинка выводит количество '
        'переходов по данной ссылке за все время.'
    )
    parser.add_argument('url', help='Длинная ссылка или битлинк.')
    args = parser.parse_args()
    return args.url


def shorten_link(token: str, url: str) -> str:
    """Return bitlink for url."""
    bitly_headers = {'Authorization': f'Bearer {token}'}
    request_body = {"long_url": url}
    bitlink_endpoint = 'https://api-ssl.bitly.com/v4/bitlinks'
    response = requests.post(bitlink_endpoint, headers=bitly_headers,
                             json=request_body)
    response.raise_for_status()
    return response.json()['id']


def count_clicks(token: str, bitlink: str) -> int:
    """Return clicks count on bitlink for all time."""
    clicks_count_endpoint = (
        f'https://api-ssl.bitly.com/v4/bitlinks/'
        f'{bitlink}/clicks/summary'
    )
    get_params = {'unit': 'day', 'units': -1}
    bitly_headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(clicks_count_endpoint, headers=bitly_headers,
                            params=get_params)
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(token: str, url: str) -> bool:
    """Check url is bitlink."""
    if not url.startswith('bit.ly'): return False
    bitlink_information_endpoint = (
        f'https://api-ssl.bitly.com/v4/'
        f'bitlinks/{url}'
    )
    bitly_headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(bitlink_information_endpoint,
                            headers=bitly_headers)
    response.raise_for_status()
    return response.ok


def main() -> None:
    """Print bitlink for your url or total clicks count
    for your bitlink.
    """
    token = os.getenv('BITLY_TOKEN')
    url = get_url()
    url_components = urlparse(url)
    netloc_plus_path = url_components.netloc + url_components.path
    try:
        if is_bitlink(token, netloc_plus_path):
            total_clicks_count = count_clicks(token, netloc_plus_path)
            print(f'По вашей ссылке прошли {total_clicks_count} раз(а)')
        else:
            bitlink = shorten_link(token, url)
            print('Битлинк', bitlink)
    except requests.exceptions.HTTPError:
        print('Некорректная ссылка')
        exit(1)


if __name__ == '__main__':
    load_dotenv()
    main()
