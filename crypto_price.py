import json
import requests

valid_coins = ["bitcoin", "ethereum", "usd-coin", "matic-network", "tezos", "pax-gold", "elrond-erd-2", "qowatt", "maiar-dex", "holoride"]

def historique():
    from datetime import datetime
    date = input("Enter the date (e.g. 30-12-2022): ")

    # Try to convert date to a datetime object
    try:
        date_obj = datetime.strptime(date, "%d%m%Y")
        date = date_obj.strftime("%d-%m-%Y")
    except ValueError:
        pass
    print(date)

    for coin in valid_coins:
        url = f"https://api.coingecko.com/api/v3/coins/{coin}/history?date={date}"
        response = requests.get(url)
        data = json.loads(response.text)

        try:
            eur_value = data["market_data"]["current_price"]["eur"]
            eur_value = round(eur_value,2)
            print(f"{coin} : {eur_value}€")
        except KeyError:
            print(f"{coin} : NA")

def actuel():
    for coin in valid_coins:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=eur"
        response = requests.get(url)
        data = json.loads(response.text)

        try:
            eur_value = data[coin]["eur"]
            eur_value = round(eur_value,2)
            print(f"{coin} : {eur_value}€")
        except KeyError:
            print(f"{coin} : NA")

while True:
    print()
    print("Choix 1 : Prix actuel")
    print("Choix 2 : Prix historique")
    print("Choix 3 : quitter le script")
    print()
    choice = input("Entrez votre choix (1, 2 ou 3) : ")

    if choice == "1":
        actuel()
    elif choice == "2":
        historique()
    elif choice == "3":
        break
    else:
        print("Choix non valide, veuillez réessayer")