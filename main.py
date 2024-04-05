import requests
from pprint import pprint

from notification_manager import NotificationManager
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch

    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

flight_search = FlightSearch()


for destination in sheet_data:
    flight = flight_search.look_for_flights(destination["iataCode"])
    if flight.price < destination["lowestPrice"]:
        notification_manager = NotificationManager()
        notification_manager.send_message(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}."
        )






