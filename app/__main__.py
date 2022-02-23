import json
import re

from bs4 import BeautifulSoup
import requests

def extract_cyrillic(words):
    return map(lambda word: re.sub(r'[^\u0400-\u04FF]', '', word), words)

def main():
    #url = input('Enter url: ')
    #selector = input('Enter selector: ')
    url = 'https://properrussian.com/2016/02/%d0%bf%d1%8f%d1%82%d1%8c-%d0%bc%d0%b8%d0%bd%d1%83%d1%82-%d0%b2%d1%8b%d0%bf%d1%83%d1%81%d0%ba-25.html'
    selector = 'div.entry-content'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    content = soup.select_one(selector)
    words = set(extract_cyrillic(content.text.lower().split()))
    words.discard('')
    print(words)
    print(len(words))


if __name__ == '__main__':
    main()
