import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

USD = 'https://finance.rambler.ru/currencies/USD/?utm_medium=widget'
EUR = 'https://www.banki.ru/products/currency/eur/'
UAH = 'https://www.banki.ru/products/currency/uah/'
CNY = 'https://finance.rambler.ru/calculators/converter/1-CNY-RUB/'
GBP = 'https://finance.rambler.ru/calculators/converter/1-GBP-RUB/'
AMD = 'https://finance.rambler.ru/calculators/converter/1-AMD-RUB/'

load_data = 'Load data...'
rub = "₽"
exit_text = 'Press Enter: '

def start_Currency_check():
	zahn = int(input('\n''The number to be convert: '))
	print('\n''Select by number')
	print('1 - Dollar, 2 - Euro, 3 - Hryvnia, 4 - Yuan, 5 - Pound, 6 -  Armenian dram')
	change = str(input('\n''Currency: '))

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
		convert = soup.findAll("div", {"class": "currency-table__large-text"})
		uah = float(convert[0].text.replace(",", "."))
		uah_out = uah * zahn / 10
		print(uah_out, rub)
		end = input(exit_text)

	elif change == '4':
		print('\n', load_data)
		full_page = requests.get(CNY, headers=headers)
		soup = BeautifulSoup(full_page.content, 'html.parser')
		convert = soup.findAll("div", {"class": "converter-display__value"})
		cny = float(convert[1].text)
		cny_out = cny * zahn 
		print(cny_out, rub)
		end = input(exit_text)

	elif change == '5':
		print('\n', load_data)
		full_page = requests.get(GBP, headers=headers)
		soup = BeautifulSoup(full_page.content, 'html.parser')
		convert = soup.findAll("div", {"class": "converter-display__value"})
		gbp = float(convert[1].text)
		gbp_out = gbp * zahn
		print(gbp_out, rub)
		end = input(exit_text)

	elif change == '6':
		print('\n', load_data)
		full_page = requests.get(AMD, headers=headers)
		soup = BeautifulSoup(full_page.content, 'html.parser')
		convert = soup.findAll("div", {"class": "converter-display__value"})
		amd = float(convert[1].text)
		amd_out = amd * zahn
		print(amd_out, rub)
		end = input(exit_text)
	
	else:
		print('\n''There is no such currency in the register, please re-enter')
		start_Currency_check()
		
start_Currency_check()