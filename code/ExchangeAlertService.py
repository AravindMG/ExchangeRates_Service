import requests


# api url to fetch the exchange rates
def orbitremit_api_url():
    url = "https://secure.orbitremit.com/api/v2/rate.json?send_currency=NZD&payout_currency=INR"
    return url


# method to convert the response to json
def response():
    response = requests.get(orbitremit_api_url())
    data = response.json()
    return data


# method to create a list from the response json
def creating_list():
    response_list = []
    for item, value in response().items():
        if item == 'data':
            response_list.append([value['send_currency'], value['payout_currency'], value['rate'], value['quote_time'],
                                  value['expiry_time'], value['exchange_rate']])
            print(response_list)
    return response_list


# method to send the alert
def create_alert():
    if creating_list()[0][2] > '45':
        print("exchange rate is high")


if __name__ == '__main__':
    create_alert()
