import requests
from datetime import datetime
import smtplib
import time


MY_LAT = -49.349810 # Your latitude
MY_LONG = -84.226410 # Your longitude
MY_EMAIL = "annaxie652@gmail.com"
PASSWORD = "abc!@#123"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
print(iss_latitude, iss_longitude)

#Your position is within +5 or -5 degrees of the ISS position.

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])



#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    time_now = datetime.now()
    if iss_longitude + 5 >= MY_LAT >= iss_latitude - 5 and iss_longitude + 5 >= MY_LONG >= iss_longitude - 5:
        if time_now.hour >= sunset or time_now.hour <= sunrise:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject: ISS is here\n\nLook up!"
            )



