# ISS Tracker and Email Notifier
This Python script tracks the International Space Station (ISS) using its current latitude and longitude. If the ISS is within a specified range of your location and it is currently dark outside, the script sends an email notification. The project utilizes the Open Notify API for ISS location data and the Sunrise-Sunset API for sunrise and sunset times.

# Prerequisites
  1. Make sure that you have Python installed on your system.
  2. Install the required libraries using the following command: pip install requests.
  3. Set up a Gmail account to send email notifications.
  4. For security, use an App Password for Gmail. Set the generated password as the environment
     variable 'PASSWORD'.

# Configuration
  1. Update 'MY_LAT' and 'MY_LONG' with your current latitude and longitude.
  2. Replace 'MY_EMAIL' with your Gmail email address in the script.
  3. The script runs continuously and checks the ISS position every 60 seconds. You can adjust the
     sleep time in the 'time.sleep(60)' line.

# Usage
  1. Clone the Repository.
  2. Replace 'MY_EMAIL' with your Gmail email address in the script.
  3. Run the script.
  4. For automated execution, consider using a cloud service like PythonAnywhere. Set up a
     scheduled task to run the script at regular intervals.

# Notes
The script retrieves the current ISS position from the Open Notify API.
It checks if the ISS is within a specified range of your location and if it is currently dark outside based on sunrise and sunset times.
f both conditions are met, an email notification is sent to alert you to look up at the sky.
