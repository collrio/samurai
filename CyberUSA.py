# -*- coding: utf-8 -*-
from colorama import init
from termcolor import colored
import requests
import html2text
import bs4
import os
import time
init()
os.system('clear')
banner =colored("Разработчик: CyberUSA\nVK: https://vk.com/CyberUSA\nТелеграм: @CyberUSA\n\n",'blue')
print(banner)
print(colored("CYBER DEANONE V 2.0\n","red"))

m = input(colored("РЕЖИМЫ:\n", 'green') + """
0 - выход\n
1 - вывод всех данных\n
2 - вывод даты публикации и адреса\n
Введите номер режима: """)
if m=="0":
	os.system('clear')
	exit(0)

def avito():
	global m
	phone = input("\n Введите номер: +7")
	res = requests.get("https://mirror.bullshit.agency/search_by_phone/" +str(phone))
	b=bs4.BeautifulSoup(res.text, "html.parser")
	operator(phone)
	time.sleep(4)
	t = b.select('h4')
	p = b.select('p')
	for i in range(len(t)):
		if m == '2':
			print(colored("Объявление "+ str(i+1) + "\n","red"))
			print(colored("Адрес: "+ p[i].select('span')[0].getText(),"green"))
			print(colored("Дата Публикации: "+ p[i].select('span')[1].getText(),"green"))
		else:
			print(colored("Объявление "+ str(i+1) + "\n","red"))
			print(colored("Название: "+ t[i].getText(),"blue"))
			print(colored("Адрес: "+ p[i].select('span')[0].getText(),"green"))
			print(colored("Дата Публикации: "+ p[i].select('span')[1].getText(),"green"))

def operator(phone):
	res = requests.get("https://tel-search.ru/numbers/phone=" + str(phone))
	b=bs4.BeautifulSoup(res.text, "html.parser")
	p = b.select("div[class~=jumbotron] > h2")
	k = 0
	print(colored("Данные по номеру:",'blue'))
	print(colored(p[0].getText(),'yellow'))
	print('\n')
avito()
time.sleep(1)
x = input("\nНажмите ENTER")
if x=="":
	os.system('clear')
	exit(0)
