import requests
from datetime import datetime, timedelta
from flight_data import FlightData
from notification_manager import NotificationManager

kiwi_api_key = "nMa4wBmAwMo6Y-q1V8Cx9sWNDHe5uBRU"
kiwi_endpoint = "https://api.tequila.kiwi.com"


class FlightSearch:

    def get_destination_code(self, city_name):
        location_endpoint = f"{kiwi_endpoint}/locations/query"
        kiwi_headers = {
            "apikey": "nMa4wBmAwMo6Y-q1V8Cx9sWNDHe5uBRU"
        }
        kiwi_parameters = {
            "term": city_name,
            "location_types": "city"
        }
        kiwi_response = requests.get(url=location_endpoint,
                                     params=kiwi_parameters,
                                     headers=kiwi_headers
                                     )
        results = kiwi_response.json()["locations"]
        code = results[0]["code"]
        return code

    def look_for_flights(self, destination_city_code):
        now = datetime.now()
        tomorrow = (now + timedelta(days=1)).strftime("%d/%m/%Y")
        six_months_later = (now + timedelta(days=180)).strftime("%d/%m/%Y")
        tequila_parameters = {
            "fly_from": "LON",
            "fly_to": destination_city_code,
            "date_from": tomorrow,
            "date_to": six_months_later,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": "GBP",
        }
        search_endpoint = f"{kiwi_endpoint}/search"
        search_headers = {
            "apikey": kiwi_api_key
        }
        response = requests.get(url=search_endpoint,
                                params=tequila_parameters,
                                headers=search_headers
                                )
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
