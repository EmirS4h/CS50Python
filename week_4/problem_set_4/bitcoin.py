import requests
import sys

args = sys.argv
if len(args) > 1:
    try:
        number_of_bitcoins = float(args[1])
        response = requests.get(
            "https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        price = float(data.get("bpi").get("USD").get(
            "rate_float")) * number_of_bitcoins
        print(f"${price:,.4f}")
    except ValueError:
        sys.exit("ERROR! : Cannot convert to float!")
else:
    print("Missing command-line argument")
