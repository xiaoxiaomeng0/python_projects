# # This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
#
# from data_manager import DataManager
# from flight_search import FlightSearch
# from notification_manager import NotificationManager
# from flight_data import FlightData
#
# from pprint import pprint
#
# data_manager = DataManager()
# lowest_price_data = data_manager.lowest_price_request()
# flight_data = FlightData()
#
# for item in lowest_price_data:
#     if not item["iataCode"]:
#         item["iataCode"] = flight_data.iata_code(item["city"])
#         data_manager.update_iata_code(item)
#
# # pprint(lowest_price_data)
#
#
# flight_search = FlightSearch(lowest_price_data, 1)
# results = flight_search.flight_request()
# print(results)
# # if len(results) == 0:
# #     flight_search = FlightSearch(lowest_price_data, 30*6)
# #     results = flight_search.flight_request()
# #     print(flight_search.future)
#
# # if len(results) == 0:
# #     notification_manager = NotificationManager(results)
# #     notification_manager.send_message()

from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager


ORIGIN_CITY_IATA = "LON"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()

if sheet_data[0]["iataCode"] == "":
    city_names = [row["city"] for row in sheet_data]
    data_manager.city_codes = flight_search.get_destination_codes(city_names)
    data_manager.update_destination_codes()
    sheet_data = data_manager.get_destination_data()

destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"]
    } for data in sheet_data}

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=6 * 30)

for destination_code in destinations:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination_code,
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight is None:
        continue

    if flight.price < destinations[destination_code]["price"]:
        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."

        ######################
        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
            print(message)
        #######################

        notification_manager.send_sms(message)