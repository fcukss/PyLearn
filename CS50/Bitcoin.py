import sys
import requests

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        number_of_bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get("https://api.coincap.io/v2/assets/bitcoin")
        response.raise_for_status()
        data = response.json()
        price_usd = float(data['data']['priceUsd'])
    except requests.RequestException:
        sys.exit("Couldn't complete request")
    except (KeyError, TypeError, ValueError):
        sys.exit("Error parsing the response")

    total_cost = number_of_bitcoins * price_usd

    print(f"${total_cost:,.4f}")

if __name__ == "__main__":
    main()