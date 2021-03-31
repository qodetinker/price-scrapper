import requests
from bs4 import BeautifulSoup
import config as c


def get_price(url_list, html_class, og_price):
    ori_price = int(og_price)
    # Pass in the URL value
    for color, url in url_list.items():
        if requests.get(url) == 200:
            page = requests.get(url)

            soup = BeautifulSoup(page.content, 'html.parser')
        
            for x in html_class.values():
                tags = soup.find_all(class_=x)

                for i in tags:
                    c_price = float(i.string[1:])
                    if c_price < ori_price:
                        print(f'There is a sale on {color}, the price is now {i.string}')


if __name__ == '__main__':
    # Nike Long Sleeves
    get_price(c.nike_long_sleeves, c.nike_price_class, 35)