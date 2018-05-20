from bs4 import BeautifulSoup

import requests


def get_page(html_link):
    # get content of page
    return requests.get(html_link)


def parse_page(page):
    # parse page with BeautifulSoup
    return BeautifulSoup(page.text, 'lxml')


def post_to_page(page, file_to_send):

    headers = {'Authorization': 'Token e61c421a7d9d1de7fd7249b8bdb185f7',
               'Accept': 'application/json',
               'Content-Type': 'application/json'}

    return requests.post(page,
                         data=open(file_to_send, 'rb'), headers=headers)
