# -*- coding: utf-8 -*-

from colorama import init
from termcolor import colored
import requests
import html2text
import bs4
import os
import time

banner = colored("Разработчик: CyberUSA && xsestech\nVK: https://vk.com/CyberUSA\nТелеграм: @CyberUSA\n\n", 'blue')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def avito(mode):
    phone = input("\n Введите номер: +7")
    res = requests.get("https://mirror.bullshit.agency/search_by_phone/" + str(phone))
    
    b = bs4.BeautifulSoup(res.text, "html.parser")
    print("Подождите, собираются данные\n")
    operator(phone)
    print()
    a = b.find_all(href=True, rel="nofollow")[0]['href']
    resn = requests.get("https://mirror.bullshit.agency" + str(a))
    n = bs4.BeautifulSoup(resn.text, "html.parser")
    name = n.select('strong')[0].getText()
    t, p = b.select('h4'), b.select('p')


    print(colored("Имя: ", 'red') + colored(name, 'blue') + "\n")
    for i in range(len(t)):
        print(colored("Объявление " + str(i+1), "red"))

        if mode == '1':
            print(colored("Название: " + t[i].getText(), "blue"))

        print(colored("Адрес: " + p[i].select('span')[0].getText(), "green"))
        print(colored("Дата Публикации: " + p[i].select('span')[1].getText(), "green"))


def operator(phone):
    res = requests.get("https://tel-search.ru/numbers/phone=" + str(phone))
    b = bs4.BeautifulSoup(res.text, "html.parser")
    p = b.select("div[class~=jumbotron] > h2")
    print(colored("Данные по номеру:", 'blue'))
    print(colored(p[0].getText(), 'yellow'))


if __name__ == '__main__':
    init()
    clear()

    print(banner)
    print(colored("CYBER DEANONE V 2.0\n", "red"))

    mode = input(colored("РЕЖИМЫ:", 'green') + """
    0 - выход
    1 - вывод всех данных
    2 - вывод даты публикации и адреса
    Введите номер режима: """)

    if mode != "0":
        avito(mode)
        x = input("\nНажмите ENTER для выхода")
    clear()
