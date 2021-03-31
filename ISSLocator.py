import requests
import json
from datetime import datetime

def main():
    #obtain the API connection to the ISS's location
    response = requests.get("http://api.open-notify.org/iss-now.json")

    #check if there is an error -> if not display a success message
    if (response.status_code == 200):
        print("No errors connecting to the ISS api")
        print(". . .")

    #transfer the response to json format
    #store the latitude and longitude into variables
    response = response.json()
    current_latitude = response["iss_position"]["latitude"]
    current_longitude = response["iss_position"]["longitude"]

    #obtain and convert the date and time to a readable format
    date_accessed = response["timestamp"]
    date_accessed = datetime.fromtimestamp(date_accessed)

    #print out the date and time that the location was accessed
    print(f"Location accessed: {date_accessed}")

    #print out the latitude and longitude to the console
    print(f"Latitude: {current_latitude} Longitude: {current_longitude}")

if __name__ == "__main__":
    main()
