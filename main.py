import requests
from datetime import datetime
import smtplib
import time
import os

MY_LAT = 52.939915 # Your latitude
MY_LONG = -73.549133 # Your longitude
MY_EMAIL = "msanoko5@gmail.com"
PASSWORD = os.environ.get("PASSWORD", "Key does not exist.")

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
iss_latitude = int(iss_latitude)
iss_longitude = int(iss_longitude)

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) - 4
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) - 4


time_now = datetime.now()
hour_now = time_now.hour

upper_bound_lat = int(MY_LAT + 5)
lower_bound_lat = int(MY_LAT - 5)
upper_bound_lng = int(MY_LONG + 5)
lower_bound_lng = int(MY_LONG - 5)

dark_outside = hour_now >= sunset


def send_email():
    close_to_position = iss_latitude in range(lower_bound_lat, upper_bound_lat + 1) and iss_longitude in range(lower_bound_lng, upper_bound_lng + 1)

    if dark_outside and close_to_position:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                                msg="Subject:ISS in your area!\n\nLook up to the sky you will see the ISS.")


if dark_outside:
    while True:
        send_email()

        time.sleep(60)

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



