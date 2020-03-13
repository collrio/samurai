# -*- coding: utf-8 -*-



#Привет юный кодер если ты залез посмотреть код 
#Это значит что ты хочешь его спиздить
#Поэтому прошу тебя укажи меня в своем проекте @CyberUSA
#Или оставь ссылку на меня
#
#Если же ты не кодер, а простой юзер извини 
#
#Если нужна помощь пишите мне в лс 
#Телеграм @CyberUSA
#
#Если у тебя есть идеи что добавить пишите
#
from pyrogram import Client
from pyrogram import InputPhoneContact
from Crypto import Random
from Crypto.Cipher import AES
from termcolor import colored
import requests
import bs4
import os
import time
import json
import urllib.request
import base64
import hmac
import hashlib
import binascii
import json
import sys
banner = colored("Разработчик: CyberUSA\nVK: https://vk.com/CyberUSA\nТелеграм: @CyberUSA\n\n", 'yellow')
menu_text = colored("РЕЖИМЫ:", 'green') + """
0 - выход
1 - вывод всех данных
2 - вывод даты публикации и адреса
Введите номер режима: """



app = Client("user")
##Получаем телеграм 
def telegram_phone(phone):
	app.start()
	app.add_contacts([InputPhoneContact(phone, "Foo")])
	contacts = app.get_contacts()
	global ide
	for x in contacts:
		try:
			ide = "@" +x.username
			print("\nТелеграм: "+ ide)
			app.delete_contacts([x.id])
		except:
			ide = "не найден или скрыт"
			print("\nТелеграм "+ ide)
			app.delete_contacts([x.id])
	app.stop()

AES_KEY = 'e62efa9ff5ebbc08701f636fcb5842d8760e28cc51e991f7ca45c574ec0ab15c' 
TOKEN = 'gWFDtf18f16d9c97c01a58948fee3c6201094e93d6d3f102177c5778052'

key = b'2Wq7)qkX~cp7)H|n_tc&o+:G_USN3/-uIi~>M+c ;Oq]E{t9)RC_5|lhAA_Qq%_4'


class AESCipher(object):

    def __init__(self, AES_KEY): 
        self.bs = AES.block_size
        self.AES_KEY = binascii.unhexlify(AES_KEY)

    def encrypt(self, raw):
        raw = self._pad(raw)
        cipher = AES.new(self.AES_KEY, AES.MODE_ECB)
        return base64.b64encode(cipher.encrypt(raw.encode()))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        cipher = AES.new(self.AES_KEY, AES.MODE_ECB)
        return self._unpad(cipher.decrypt(enc)).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]


aes = AESCipher(AES_KEY)

def sendPost(url, data, sig, ts):
    headers = {'X-App-Version': '4.9.1',
        'X-Token':TOKEN,
        'X-Os': 'android 5.0',
        'X-Client-Device-Id': '14130e29cebe9c39',
        'Content-Type': 'application/json; charset=utf-8',
        'Accept-Encoding': 'deflate',
        'X-Req-Timestamp': ts,
        'X-Req-Signature': sig,
        'X-Encrypted': '1'}
    r = requests.post(url, data=data, headers=headers, verify=True)
    return json.loads(aes.decrypt(r.json()['data']))

def getByPhone(phone):
    ts = str(int(time.time()))
    req = f'"countryCode":"RU","source":"search","token":"{TOKEN}","phoneNumber":"{phone}"'
    req = '{'+req+'}'
    string = str(ts)+'-'+req
    sig = base64.b64encode(hmac.new(key, string.encode(), hashlib.sha256).digest()).decode()
    crypt_data = aes.encrypt(req)
    return sendPost('https://pbssrv-centralevents.com/v2.5/search',
                    b'{"data":"'+crypt_data+b'"}', sig, ts)

def getByPhoneTags(phone):
    ts = str(int(time.time()))
    req = f'"countryCode":"RU","source":"details","token":"{TOKEN}","phoneNumber":"{phone}"'
    req = '{'+req+'}'
    string = str(ts)+'-'+req
    sig = base64.b64encode(hmac.new(key, string.encode(), hashlib.sha256).digest()).decode()
    crypt_data = aes.encrypt(req)
    return sendPost('https://pbssrv-centralevents.com/v2.5/number-detail',
                    b'{"data":"'+crypt_data+b'"}', sig, ts)



##Получаем GETCONTACT
def main(phone):
	if '+' not in phone:
		phone = '+'+phone
	clear()
	print(colored('\n========GETCONTACT========', 'yellow'))
	finfo = getByPhone(phone)
	try:
		if finfo['result']['profile']['displayName']:
			print(finfo['result']['profile']['displayName'])
			print('Тегов найдено: '+str(finfo['result']['profile']['tagCount']))
			try:
				print('\n'.join([i['tag'] for i in getByPhoneTags(phone)['result']['tags']]))
			except KeyError:
				if finfo['result']['profile']['tagCount'] > 0:
					print('Теги найдены, но для просморта нужен премиум')
				else:
					print('Тегов не найдено!')
		else:
			print('Не найдено!')
		print('Осталось обычных поисков: '+str(finfo['result']['subscriptionInfo']['usage']['search']['remainingCount'])+'/'+str(finfo['result']['subscriptionInfo']['usage']['search']['limit']))
		print(colored('\n========AVITO=========', 'yellow'))
	except:
		print('Не найдено!')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
##Парсим Авито
def avito(mode):
    phone = input("\nВведите номер: +7")
    p = "7"+phone
    main(str(p))
    try:
    	res = requests.get("https://mirror.bullshit.agency/search_by_phone/" + str(phone))
    	b = bs4.BeautifulSoup(res.text, "html.parser")
    	print("Поиск данных на Авито")
    	a = b.find_all(href=True, rel="nofollow")[0]['href']
    	resn = requests.get("https://mirror.bullshit.agency" + str(a))
    	n = bs4.BeautifulSoup(resn.text, "html.parser")
    	name = n.select('strong')[0].getText()
    	t, p = b.select('h4'), b.select('p')
    	print(colored("Имя: ", 'white') + colored(name, 'white') + "\n")
    	for i in range(len(t)):
    		print(colored("Объявление " + str(i+1), "white"))
    		if mode == '1':
    			print(colored("Название: " + t[i].getText(), "white"))
    			print(colored("Адрес: " + p[i].select('span')[0].getText(), "green"))
    			print(colored("Дата Публикации: " + p[i].select('span')[1].getText(), "green"))
    except:
    	print(colored("На авито не найдено данных!", "white"))
    print(colored('\n=========SIM=========\n', 'yellow'))
    operator(phone)
    print(colored('\n======================', 'yellow'))

##Парсим данные по номеру
def operator(phone):
	try:
		getInfo = "https://htmlweb.ru/geo/api.php?json&telcod=7" + str(phone)
		try:
			infoPhone = urllib.request.urlopen( getInfo )
		except:
			print( "\nТелефон не найден\n" )
		infoPhone = json.load( infoPhone )
		print( u"Страна:", infoPhone["country"]["name"] )
		print( u"Регион:", infoPhone["region"]["name"] )
		print( u"Округ:", infoPhone["region"]["okrug"] )
		print( u"Оператор:", infoPhone["0"]["oper"] )
		print( u"Часть света:", infoPhone["country"]["location"] )
	except:
		print(colored("Неизвестная ошибка попробуйте снова!", "white"))


if __name__ == '__main__':
    clear()

    print(banner)
    print(colored("CYBER DEANONE V 3.0\n", "red"))

    mode = input(menu_text)
    if mode != "0":
        avito(mode)
        print("Для поиска аккаунта телеграм нужен VPN\n")
        print("Для поиска введите: yes")
        action = input("Найти Telegram Аккаунт? ")
        if action == "yes":
        	print(colored('\n========TELEGRAM=========', 'yellow'))
        	phone = input("Введите номер: +7")
        	telegram_phone("7"+ phone)
        	print(colored('\n======================', 'yellow'))
        	x = input("\nНажмите ENTER для выхода")
        else:
        	x = input("\nНажмите ENTER для выхода")
        	clear()
