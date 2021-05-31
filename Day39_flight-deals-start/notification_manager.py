from twilio.rest import Client
import os
from dotenv import load_dotenv
import flight_search

load_dotenv()


account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, flight_list:flight_search):
        self.flight_list = flight_list

    def send_message(self):
        for flight in self.flight_list:
            message = client.messages.create(
                body="LOW PRICE ALERT!\n"
                     f"from {self.flight['flyFrom']} to {self.flight['flyTo']}\n"
                     f"price: EUR {self.flight['price']}\n"
                     f"Departure at: {self.flight['local_departure']}\n"
                     f"Arrive at {self.flight['local_arrival']}",
                from_="+14075054806",
                to="+18144415603"
            )