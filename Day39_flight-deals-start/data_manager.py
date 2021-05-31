# import requests
#
# flight_data_url = "https://api.sheety.co/42249d81205f4e5645dfcd92aee2ca5b/flightPrices/prices"
#
#
# class DataManager:
#     # This class is responsible for talking to the Google Sheet.
#     def __init__(self):
#         pass
#
#     def lowest_price_request(self):
#         response = requests.get(url=flight_data_url)
#         return response.json()["prices"]
#
#     def update_iata_code(self, flight_data):
#         data = {
#             "price": flight_data,
#         }
#         response = requests.put(url=f"{flight_data_url}/{flight_data['id']}", json=data)
#         print(response.text)

from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = YOUR SHEETY PRICES ENDPOINT


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
