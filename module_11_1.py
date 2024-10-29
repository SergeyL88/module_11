from bs4 import BeautifulSoup as bs
from simple_term_menu import TerminalMenu as tm
import numpy
import pandas as pd
import requests

menu_list: list = ['1) Requests/BS4', '2) Numpy', '3) Pandas']
terminal_menu = tm(menu_list)
menu_entry = terminal_menu.show()
if menu_entry == 0:
    # REQUESTS/BS4

    URL = 'https://www.avito.ru'
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    try:
        req = requests.get(url=URL, headers=HEADERS)
    except ConnectionError:
        print('Connection Error')

    soup = bs(req.text)
    print(soup)
elif menu_entry == 1:
    # Numpy

    array_1 = numpy.array([[5, 6, 7], [1, 2, 3]])
    array_2 = numpy.array([[3, 7, 9], [4, 8, 2]])
    print(array_1 + array_2)
elif menu_entry == 2:
    # Pandas

    price_list = pd.read_csv('price_list.txt')
    print(price_list)
