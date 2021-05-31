# import requests
# from dotenv import load_dotenv
# import os
#
# load_dotenv()
#
#
# class FlightData:
#     # This class is responsible for structuring the flight data.
#     def __init__(self):
#         pass
#
#     def iata_code(self, city):
#         location_api = "https://tequila-api.kiwi.com/locations/query"
#         header = {
#             "apikey": os.environ.get("FLIGHT_APIKEY"),
#             "content-encoding": "gzip",
#         }
#         parameters = {
#             "term": city
#         }
#         response = requests.get(url=location_api, params=parameters, headers=header)
#
#         return response.json()["locations"][0]["code"]

class FlightData:

    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date,
                 stop_overs=0, via_city=""):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

        self.stop_overs = stop_overs
        self.via_city = via_city§