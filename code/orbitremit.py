import requests

orbitRemit_rate_url = "https://secure.orbitremit.com/api/v2/rate.json?send_currency=NZD&payout_currency=INR"
response = requests.get(orbitRemit_rate_url)
data = response.json()

if __name__ == "__main__":
    print(data)
    for item, value in data.items():
        if item == 'data':
            print("send_currency = " + value['send_currency'])
            print("payout_currency = " + value['payout_currency'])
            print("rate = " + value['rate'])
            print("quote_time = " + value['quote_time'])
            print("expiry_time = " + value['expiry_time'])
            print("exchange_rate = " + value['exchange_rate'])
    # for item, value in data['data'].items():
    #     print(item + " = ", value)
    #     if item == 'rate':
    #         print(value)
