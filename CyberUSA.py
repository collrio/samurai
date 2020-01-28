import requests
import html2text
import bs4
import os
os.system('clear')
banner = 'Разработчик: CyberUSA\nVK: https://vk.com/CyberUSA\nТелеграм: @CyberUSA\n\n'

print(banner)
print('CYBER DEANONE V 1.1')

def avito():
	print('Парсер данных с авито\n')
	phone = input('Введите номер: +7')
	res = requests.get('https://mirror.bullshit.agency/search_by_phone/' + phone)
	b=bs4.BeautifulSoup(res.text, "html.parser")

	p = b.select('.text-muted')
	k = 0
	for i in p:
		ps = p[k].getText()
		print(ps.strip())
		k=k+1

##avito(phone)
##input('Нажмите что бы продолжить')


def operator():
	
	phone = input('Введите номер: +7')
	res = requests.get('https://tel-search.ru/numbers/phone=' + phone)
	b=bs4.BeautifulSoup(res.text, "html.parser")
	p = b.select('.jumbotron')
	k = 0
	os.system('clear')
	print('Данные по номеру\n\n')
	for i in p:
		ps = p[k].getText()
		print(ps.strip(), '\n\n')
		k=k+1
		
		
operator()
input('\nНажмите ENTER\n\n')
os.system('clear')
avito()
