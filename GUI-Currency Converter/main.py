#!/usr/bin/env python3
import eel
import requests
from bs4 import BeautifulSoup


eel.init("web")

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

USD = 'https://finance.rambler.ru/currencies/USD/?utm_medium=widget'
EUR = 'https://www.banki.ru/products/currency/eur/'
UAH = 'https://www.banki.ru/products/currency/uah/'
CNY = 'https://finance.rambler.ru/calculators/converter/1-CNY-RUB/'
GBP = 'https://finance.rambler.ru/calculators/converter/1-GBP-RUB/'
AMD = 'https://finance.rambler.ru/calculators/converter/1-AMD-RUB/'
CAD = 'https://www.banki.ru/products/currency/cad/'
CHF = 'https://www.banki.ru/products/currency/chf/'


@eel.expose
def check_Dollar():
    full_page = requests.get(USD, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert_usd = soup.findAll("div", {"class": "finance-currency-plate__currency"})
    out = float(convert_usd[0].text)
    return out

@eel.expose
def check_Euro():
    full_page = requests.get(EUR, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert_eu = soup.findAll("div", {"class": "currency-table__large-text"})
    out = float(convert_eu[0].text.replace(",", "."))
    return out

@eel.expose
def check_Pound():
    full_page = requests.get(GBP, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("div", {"class": "converter-display__value"})
    out = float(convert[1].text)
    return out

@eel.expose
def check_Hryvnia():
    full_page = requests.get(UAH, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("div", {"class": "currency-table__large-text"})
    uah = float(convert[0].text.replace(",", "."))
    out = uah / 10
    return out

@eel.expose
def check_Yuan():
    full_page = requests.get(CNY, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("div", {"class": "converter-display__value"})
    out = float(convert[1].text)
    return out

@eel.expose
def check_ArmenianDram():
    full_page = requests.get(AMD, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("div", {"class": "converter-display__value"})
    out = float(convert[1].text)
    return out

@eel.expose
def check_CanadianDollar():
    full_page = requests.get(CAD, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert_eu = soup.findAll("div", {"class": "currency-table__large-text"})
    out = float(convert_eu[0].text.replace(",", "."))
    return out

@eel.expose
def check_SwissFrank():
    full_page = requests.get(CHF, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert_eu = soup.findAll("div", {"class": "currency-table__large-text"})
    out = float(convert_eu[0].text.replace(",", "."))
    return out





eel.start("main.html", size=(1000, 700))