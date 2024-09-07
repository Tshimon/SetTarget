import requests

API_KEY = 'your_api_key_here'
BASE_URL = '<https://api.sbisec.co.jp/v1/>'

def get_stock_price(stock_code):
    endpoint = f'{BASE_URL}stock/{stock_code}/price'
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    response = requests.get(endpoint, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

stock_code = '7203'  # トヨタ自動車の例
price_info = get_stock_price(stock_code)
if price_info:
    print(f"Stock Price for {stock_code}: {price_info['price']}")
else:
    print("Failed to retrieve stock price.")