# This code parsing site nbrb.by and get BYN exchange rates

import requests
import json


currency = input("ISO_4217 currency name:\n").upper()
url = "https://www.nbrb.by/api/exrates/rates/" + currency + "?parammode=2"


def get_currency(some_url):

    """"
    :param some_url: url according to which make get request
    :type some_url: str
    :return: currency in string format
    :rtype: str
    """

    response = requests.get(some_url)
    if response.status_code == 200:
        data = json.loads(response.text)
        print(data.get("Cur_Scale"), data.get("Cur_Abbreviation"), "-", data.get("Cur_OfficialRate"), "BYN at",
              data.get("Date"))
    else:
        print("Input correct data or data not found")


if __name__ == "__main__":
    get_currency(url)
