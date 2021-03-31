import requests
from geopy.geocoders import Nominatim
from datetime import datetime

def main():
    #obtain the API connection to the ISS's location
    loc_response = requests.get("http://api.open-notify.org/iss-now.json")

    #obtain the API connection to the number of people in space
    people_response = requests.get("http://api.open-notify.org/astros.json")

    #check if there is an error -> if not display a success message
    if (loc_response.status_code == 200):
        print("No errors connecting to the ISS api")
        print(". . .")
    else:
        print("There was an error connecting to the ISS api")

    #transfer the response to json format
    #store the latitude and longitude into variables
    loc_response = loc_response.json()
    people_response = people_response.json()
    
    #display the position and date accessed
    display_pos_and_time(loc_response)

    #display how many people are in space currently
    display_num_people(people_response)

def display_pos_and_time(response):
    #initialize Nominatim API
    geolocator = Nominatim(user_agent = "geoapiExercises")

    latitude = response["iss_position"]["latitude"]
    longitude = response["iss_position"]["longitude"]

    #obtain and convert the date and time to a readable format
    date_accessed = response["timestamp"]
    date_accessed = datetime.fromtimestamp(date_accessed)

    #print out the date and time that the location was accessed
    print(f"Location accessed on: {date_accessed}")

    #print out the latitude and longitude to the console
    print(f"Latitude: {latitude} Longitude: {longitude}")

    #discover location with geopy
    location = geolocator.reverse(f"{latitude},{longitude}")

    #try to access the address, if not possible it is over an ocean
    try:
        #access the address and some of its components
        address = location.raw["address"]
        city = address.get("city")
        state = address.get("state")
        country = address.get("country")

        #print out the city, state and country
        print(f"City it is over: {city}")
        print(f"State it is over: {state}")
        print(f"Country it is over: {country}")

    except:
        print("It is currently over an ocean")

def display_num_people(response):
    #obtain the number of people in space from api
    num_people = response["number"]

    #print out how many people are in space right now
    print(f"There are {num_people} people in space right now")

if __name__ == "__main__":
    main()
