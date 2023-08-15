#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
from datetime import datetime
import reverse_geocoder as rg

URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp = requests.get(URL).json()
    
    # SOLUTION TO PART 2
    lon = resp["iss_position"]["longitude"]
    lat = resp["iss_position"]["latitude"]

    timeS = resp["timestamp"]
    timeS = datetime.datetime.fromtimestamp(timeS)

    locator_resp = rg.search((lat, lon))

    city = locator_resp[0]["name"]

    country = locator_resp[0]["cc"]


    print(f"""
    CURRENT LOCATION OF THE ISS:
    Time: {timeS}
    Longitude: {lon}
    Latitude: {lat}
    Geographical Location: {city}, {country}
    """)

if __name__ == "__main__":
    main()
