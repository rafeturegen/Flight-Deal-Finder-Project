class NotificationManager:
    def send_message(self, message):
        from twilio.rest import Client
        from flight_data import FlightData
        account_sid = 'secret'
        auth_token = 'secret'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=message,
            from_='+12765288768',
            to='+secret'
        )

