import requests

def get_price(crypto_id):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    if crypto_id not in data:
        print(f"Error: Invalid cryptocurrency ID '{crypto_id}'")
        return None
    else:
        return data[crypto_id]["usd"]

crypto_id = input("Enter the cryptocurrency ID (e.g., bitcoin): ")
price = get_price(crypto_id)
if price:
    print(f"The current price of {crypto_id.capitalize()} is ${price:.2f}")
