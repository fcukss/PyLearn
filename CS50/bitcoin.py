import sys
import requests

#
# def get_bitcoin_price():
#     user_input = input().strip()
#     if not user_input:
#         sys.exit("Missing command-line argument")
#     try:
#         number = float(user_input)
#     except ValueError:
#         sys.exit("Command-line argument is not a number")
#     try:
#         response =  requests.get(" https://api.coincap.io/v2/assets/bitcoin")
#         response.raise_for_status()
#     except requests.RequestException:
#         sys.exit("couldn't complete request")
#     content = response.json()
#     index = content['data'].get('priceUsd')
#     amount = number*float(index)
#     print(f"${amount:,.4f}")
#
#
#
# get_bitcoin_price()


def main():
    # Проверяем наличие аргумента командной строки
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    # Пытаемся преобразовать аргумент в число с плавающей точкой
    try:
        number_of_bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # Выполняем запрос к API CoinCap для получения текущей цены биткойна
    try:
        response = requests.get("https://api.coincap.io/v2/assets/bitcoin")
        response.raise_for_status()
        data = response.json()
        price_usd = float(data['data']['priceUsd'])
    except requests.RequestException:
        sys.exit("Couldn't complete request")
    except (KeyError, TypeError, ValueError):
        sys.exit("Error parsing the response")

    # Рассчитываем стоимость покупки
    total_cost = number_of_bitcoins * price_usd

    # Выводим результат с точностью до четырех знаков после запятой и разделителями тысяч
    print(f"${total_cost:,.4f}")

if __name__ == "__main__":
    main()
