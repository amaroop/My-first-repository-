from bs4 import BeautifulSoup
import requests


def get_rate(in_currency, out_currency):
    url = f"https://www.x-rates.com/calculator/?from{in_currency}, {out_currency}&amount=1"
    request = requests.get(url).content
    soup = BeautifulSoup(request, "html.parser").find("span",class_="ccOutputRslt").get_text()
    rate = float(soup[:-4])
    return rate


def main():
    in_currency= input("enter from currency code")
    out_currency = input("enter to currency code")
    return get_rate(in_currency , out_currency)

print (main())
