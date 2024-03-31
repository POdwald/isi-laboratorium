import requests
from bs4 import BeautifulSoup

def find_links(url):
    links = []
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a'):
            href = link.get('href')
            if href:
                links.append(href)
        return links
    except Exception as e:
        print('Wystapil blad podczas analizowania strony:', e)
        return None

if __name__ == '__main__':
    url = 'https://example.com'

    found_links = find_links(url)
    if found_links:
        print('Znalezione linki:')
        for link in found_links:
            print(link)
    else:
        print('Nie udalo sie znalezc linkow.')