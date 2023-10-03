import requests
import json
import sys

def main():
    money = getMoney()
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = response.json()
        rateFloat = o["bpi"]["USD"]["rate_float"]
    except requests.RequestException:
        exit()
    amount = money * rateFloat
    print(f"${amount:,.4f}")
    
    


def getMoney():
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)
        
    else:
        try:
            money = float(sys.argv[1])
            return money
        except ValueError:
            print("Command-line argument is not a number")
            exit(1)


if __name__ == "__main__":
    main()