# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from flight_data import FlightData

from pprint import pprint

data_manager = DataManager()
lowest_price_data = data_manager.lowest_price_request()
flight_data = FlightData()

for item in lowest_price_data:
    if not item["iataCode"]:
        item["iataCode"] = flight_data.iata_code(item["city"])
        data_manager.update_iata_code(item)

# pprint(lowest_price_data)


flight_search = FlightSearch(lowest_price_data, 1)
results = flight_search.flight_request()
print(results)

notification_manager = NotificationManager(results)
notification_manager.send_message()