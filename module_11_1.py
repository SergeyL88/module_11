from simple_term_menu import TerminalMenu as tm
import numpy
import pandas as pd
import requests


if __name__ == "__main__":
    while True:
        menu_list: list = ['1) Numpy', '2) Pandas', '3) Requests', '4) Exit']
        terminal_menu = tm(menu_list)
        menu_entry = terminal_menu.show()

        if menu_entry == 0:
            # Numpy

            array_1 = numpy.array([[5, 6, 7], [1, 2, 3]])
            array_2 = numpy.array([[3, 7, 9], [4, 8, 2]])
            print(f'Сложение двумерных массивов:')
            print(f'{array_1}\n  +\n{array_2}\n  =\n{array_1 + array_2}')

        elif menu_entry == 1:
            # Pandas

            price_list = pd.read_csv('price_list.txt')
            print(price_list)
        elif menu_entry == 2:
            # Requests

            site = input(f'Введите имя сайта для проверки:\n')
            try:
                req = requests.get(url=f'https://{site}', timeout=3)
                print(f'Сайт https://{site} доступен')
            except requests.exceptions.ConnectionError as e:
                print(f'Проблема с подключением к сайту: https://{
                      site}.\nПодробнее:\n{e}\n')

        elif menu_entry == 3:
            break
    print("Работа программы завершена")
