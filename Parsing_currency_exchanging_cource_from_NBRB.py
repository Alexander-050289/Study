import requests
import json

currency = input("Name of currencies (ISO_4217)\n")
url = "https://www.nbrb.by/api/exrates/rates/" + currency + "?parammode=2"

response = requests.get(url)

data = json.loads(response.text)
print(data.get("Cur_Scale"), data.get("Cur_Abbreviation"), "-", data.get("Cur_OfficialRate"), "BYN at", data.get("Date"))

