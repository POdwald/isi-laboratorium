import requests
import re  # For REGEX
from bs4 import BeautifulSoup
import csv

class Home:
    def __init__(self, header_name, price, price_per_m2):
        self.header_name = header_name
        self.price = price
        self.price_per_m2 = price_per_m2


def scrape_homes(url):
    homes = []
    # Aby obejsc response 403, należy dodać header
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    listings_divs = soup.find_all('div', class_='css-1ojmxpg e88tro02')
    if listings_divs:
        for div in listings_divs:
            # Szukanie nagłowka ogloszenia
            header_name_elem = div.find('p', class_='css-3czwt4 e1dhq2er0')
            if header_name_elem:
                header_name = header_name_elem.text.strip()
            else:
                header_name = 'N/A'
            
            # Szukanie ceny
            price_elem = div.find('span', class_='css-1uwck7i e1a3ad6s0')
            if price_elem:
                price = re.sub(r'[^\d,.]', '', price_elem.text.strip())
                if len(price) == 0:
                    price = 'N/A'
            else:
                price = 'N/A'
                
            # Szukanie ceny za metr kwadratowy
            dl_element = div.find('dl', class_='css-uki0wd e12r8p6s1')
            if dl_element:
                dt_element = dl_element.find('dt', string='Cena za metr kwadratowy')
                if dt_element:
                    dd_element = dt_element.find_next_sibling('dd')
                    if dd_element:
                        price_per_m2 = re.sub(r'[^\d,.]', '', dd_element.text.strip())
                    else:
                        price_per_m2 = 'N/A'
                else:
                    price_per_m2 = 'N/A'
            else:
                price_per_m2 = 'N/A'

            home = Home(header_name, price, price_per_m2)
            homes.append(home)
    else:
        print('Nie znaleziono żadnych ofert domów.')

    return homes

def save_to_csv(homes, file_path):
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['header_name', 'price', 'price_per_m2']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for home in homes:
            writer.writerow({
                'header_name': home.header_name,
                'price': home.price,
                'price_per_m2': home.price_per_m2
            })


if __name__ == '__main__':
    url = 'https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/pomorskie/gdynia/gdynia/gdynia?priceMax=600000&viewType=listing'
    homes = scrape_homes(url)

    if homes:
        save_to_csv(homes, 'home.csv')
        print('Pomyślnie zapisano oferty domów do pliku \'home.csv\'.')

