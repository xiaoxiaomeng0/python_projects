import requests
from dotenv import load_dotenv
import os

load_dotenv()


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        pass

    def iata_code(self, city):
        location_api = "https://tequila-api.kiwi.com/locations/query"
        header = {
            "apikey": os.environ.get("FLIGHT_APIKEY"),
            "content-encoding": "gzip",
        }
        parameters = {
            "term": city
        }
        response = requests.get(url=location_api, params=parameters, headers=header)

        return response.json()["locations"][0]["code"]
