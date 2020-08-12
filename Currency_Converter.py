import requests
from bs4 import BeautifulSoup
from tkinter import *

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

USD = 'https://finance.rambler.ru/currencies/USD/?utm_medium=widget'
EUR = 'https://www.banki.ru/products/currency/eur/'
UAH = 'https://www.banki.ru/products/currency/uah/'
CNY = 'https://finance.rambler.ru/calculators/converter/1-CNY-RUB/'

zahn = int(input('Число: '))
print('Выберите цифрой')
print('1 - Доллар, 2 - Евро, 3 - Гривна, 4 - Юань')
change = str(input('\n''Валюта: '))

load_data = 'Загрузка данных...'
rub = "₽"
exit_text = 'Press Enter: '

if change == '1':
	print('\n', load_data)
	full_page = requests.get(USD, headers=headers)
	soup = BeautifulSoup(full_page.content, 'html.parser')
	convert_usd = soup.findAll("div", {"class": "finance-currency-plate__currency"})
	usd = float(convert_usd[0].text)
	usd_out = usd * zahn
	print(usd_out, rub)
	end = input(exit_text)

elif change == '2':
	print('\n', load_data)
	full_page = requests.get(EUR, headers=headers)
	soup = BeautifulSoup(full_page.content, 'html.parser')
	convert_eu = soup.findAll("div", {"class": "currency-table__large-text"})
	eur = float(convert_eu[0].text.replace(",", "."))
	eur_out = eur * zahn
	print(eur_out, rub)
	end = input(exit_text)

elif change == '3':
	print('\n', load_data)
	full_page = requests.get(UAH, headers=headers)
	soup = BeautifulSoup(full_page.content, 'html.parser')
	convert_eu = soup.findAll("div", {"class": "currency-table__large-text"})
	uah = float(convert_eu[0].text.replace(",", "."))
	uah_out = uah * zahn / 10
	print(uah_out, rub)
	end = input(exit_text)

elif change == '4':
	print('\n', load_data)
	full_page = requests.get(CNY, headers=headers)
	soup = BeautifulSoup(full_page.content, 'html.parser')
	convert_eu = soup.findAll("div", {"class": "converter-display__value"})
	cny = float(convert_eu[1].text)
	cny_out = cny * zahn 
	print(cny_out, rub)
	end = input(exit_text)
	
else:
	print('Такой валюты нет в реестре, повторите ввод')