import requests
import json

def main():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        print(json.loads(response))
    except requests.RequestException:
        exit()

if __name__ == "__main__":
    main()