import requests

orbitremit_rate_url = "https://secure.orbitremit.com/api/v2/rate.json?send_currency=NZD&payout_currency=INR"
response = requests.get(orbitremit_rate_url)
data = response.json()

if __name__ == "__main__":
    for item, value in data['data'].items():
        print(item + " = ", value)
        if item == 'rate':
            print(value)
