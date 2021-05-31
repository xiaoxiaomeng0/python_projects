# from datetime import datetime, timedelta
# import requests
# import data_manager
# from dotenv import load_dotenv
# import os
#
# load_dotenv()
#
# flight_search_endpoint = "https://tequila-api.kiwi.com/v2/search"
#
# class FlightSearch:
#     #This class is responsible for talking to the Flight Search API.
#     def __init__(self, list:data_manager, range=30):
#         self.list = list
#         self.now = datetime.now()
#         self.range = range
#         self.future = None
#         self.cheap_flight = []
#         # self.stop_overs = stop_overs
#         # self.via_city = via_city
#
#     def day_range_cal(self):
#         self.future = self.now + timedelta(days=self.range)
#         self.now = self.now.strftime("%d/%m/%Y")
#         self.future = self.future.strftime("%d/%m/%Y")
#
#     def flight_request(self):
#         self.day_range_cal()
#         for data in self.list:
#             search_params = {
#                 "fly_from": "BOS",
#                 "fly_to": data["iataCode"],
#                 "dateFrom": self.now,
#                 "dateTo": self.future,
#                 # "max_stopovers": self.stop_overs,
#                 "flight_type": "round",
#                 # "curr": "EUR",
#                 # "select_stop_airport": self.via_city
#             }
#             headers = {
#                 "content-encoding": "gzip",
#                 "apikey": os.environ.get("FLIGHT_APIKEY"),
#             }
#             response = requests.get(url=flight_search_endpoint, params=search_params, headers=headers)
#             # try:
#             cur_lowest = response.json()["data"][0]
#             print(cur_lowest)
#             # except IndexError:
#             #     print(f"No flights found for {data['iataCode']}")
#
#             # else:
#             if cur_lowest["price"] < int(data["lowestPrice"]):
#                 flight = {
#                     "price": cur_lowest["price"],
#                     "flyFrom": cur_lowest["flyFrom"],
#                     "flyTo": cur_lowest["flyTo"],
#                     "local_arrival": cur_lowest["local_arrival"],
#                     "local_departure": cur_lowest["local_departure"],
#                 }
#                 self.cheap_flight.append(flight)
#
#         return self.cheap_flight
#
import os
from dotenv import load_dotenv
import requests
from flight_data import FlightData
from pprint import pprint

load_dotenv()


TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"


class FlightSearch:

    def __init__(self):
        self.city_codes = []

    def get_destination_codes(self, city_names):
        print("get destination codes triggered")
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": os.environ.get("FLIGHT_APIKEY")}
        for city in city_names:
            query = {"term": city, "location_types": "city"}
            response = requests.get(url=location_endpoint, headers=headers, params=query)
            results = response.json()["locations"]
            code = results[0]["code"]
            self.city_codes.append(code)

        return self.city_codes

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        print(f"Check flights triggered for {destination_city_code}")
        headers = {"apikey": os.environ["TEQUILA_API_KEY"]}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 30,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=headers,
            params=query,
        )

        try:
            data = response.json()["data"][0]
        except IndexError:

            ##########################
            query["max_stopovers"] = 1
            response = requests.get(
                url=f"{TEQUILA_ENDPOINT}/v2/search",
                headers=headers,
                params=query,
            )
            data = response.json()["data"][0]
            pprint(data)
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][1]["cityTo"],
                destination_airport=data["route"][1]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][2]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
            )
            return flight_data
            ###########################
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )

            return flight_data
