import requests
import pandas as pd

orbitRemit_rate_url = "https://secure.orbitremit.com/api/v2/rate.json?send_currency=NZD&payout_currency=INR"
response = requests.get(orbitRemit_rate_url)
data = response.json()
or_list = []

if __name__ == "__main__":
    print(data)
    for item, value in data.items():
        if item == 'data':
            or_list.append([value['send_currency'], value['payout_currency'], value['rate'], value['quote_time'],
                           value['expiry_time'], value['exchange_rate']])
            print(or_list)

    dataset = pd.DataFrame(or_list)
    dataset.columns = ['send_currency', 'payout_currency', 'rate', 'quote_time', 'expiry_time', 'exchange_rate']
    dataset.dropna(axis=0, how='any', inplace=True)
    dataset.index = pd.RangeIndex(len(dataset.index))
    dataset.sample(frac=0.5, replace=True)
    export_csv = dataset.to_csv(r"C:\Users\Admin\Documents\My_project\exchange-rate.csv", index=None, header=True)
