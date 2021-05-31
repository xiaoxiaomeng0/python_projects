import requests

flight_data_url = "https://api.sheety.co/42249d81205f4e5645dfcd92aee2ca5b/flightPrices/prices"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        pass

    def lowest_price_request(self):
        response = requests.get(url=flight_data_url)
        return response.json()["prices"]

    def update_iata_code(self, flight_data):
        data = {
            "price": flight_data,
        }
        response = requests.put(url=f"{flight_data_url}/{flight_data['id']}", json=data)
        print(response.text)