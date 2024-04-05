import requests


sheety_put_endpoint = "https://api.sheety.co/9cf9ada6ca82a34252fe81815b000949/flightDeals/prices"
SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/9cf9ada6ca82a34252fe81815b000949/flightDeals/prices"


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
            parameters = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{sheety_put_endpoint}/{city["id"]}", json=parameters)

