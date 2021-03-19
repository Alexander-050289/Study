import requests
import json
from contracts import contract

currency = input("Name of currencies (ISO_4217)\n").upper()
url = "https://www.nbrb.by/api/exrates/rates/" + currency + "?parammode=2"

def get_currency(some_currency, some_url):
    """"
    :param some_currency: currency you need to know
    :type some_currency: str
    :return: currency in string format
    :rtype: dict
    """
    response = requests.get(some_url)
    if response.status_code == 200:
        data = json.loads(response.text)
        print(data.get("Cur_Scale"), data.get("Cur_Abbreviation"), "-", data.get("Cur_OfficialRate"), "BYN at",
          data.get("Date"))
    else:
        print("Input correct data or data not found")

if __name__ == "__main__":
    get_currency(currency, url)


