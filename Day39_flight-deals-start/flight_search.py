from datetime import datetime, timedelta
import requests
import data_manager
from dotenv import load_dotenv
import os

load_dotenv()

flight_search_endpoint = "https://tequila-api.kiwi.com/v2/search"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, list:data_manager, range=30):
        self.list = list
        self.now = datetime.now()
        self.range = range
        self.future = None
        self.cheap_flight = []

    def day_range_cal(self):
        self.future = self.now + timedelta(days=self.range)
        self.now = self.now.strftime("%d/%m/%Y")
        self.future = self.future.strftime("%d/%m/%Y")

    def flight_request(self):
        self.day_range_cal()
        for data in self.list:
            search_params = {
                "fly_from": "BOS",
                "fly_to": data["iataCode"],
                "dateFrom": self.now,
                "dateTo": self.future,
                "max_stopovers": 0,
                "flight_type": "round"
            }
            headers = {
                "content-encoding": "gzip",
                "apikey": os.environ.get("FLIGHT_APIKEY"),
            }
            response = requests.get(url=flight_search_endpoint, params=search_params, headers=headers)
            cur_lowest = response.json()["data"][0]
            if cur_lowest["price"] < int(data["lowestPrice"]):
                flight = {
                    "price": cur_lowest["price"],
                    "flyFrom": cur_lowest["flyFrom"],
                    "flyTo": cur_lowest["flyTo"],
                    "local_arrival": cur_lowest["local_arrival"],
                    "local_departure": cur_lowest["local_departure"],
                }
                self.cheap_flight.append(flight)

        return self.cheap_flight


