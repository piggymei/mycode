#!/usr/bin/env python3

import requests ## 3rd party URL lookup
import pprint
import re
## define the main function
def main():
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?' # API URL
    startdate = input("what is the start date?  yyyy-mm-dd ")  ## start date for data
    enddate = '&end_date=END_DATE' ## create a mechanism to utilize enddate
    mykey = '&api_key=DEMO_KEY' ## replace this with our API key

    neourl = neourl + "start_date=" + startdate + mykey

    neojson = (requests.get(neourl)).json()

    pprint.pprint(neojson)
    prameters(neojson)
def prameters(neojson):
    
    for objects in neojson["near_earth_objects"].values():
        for asteroid in objects:
           
           num_moonlength = float( asteroid["close_approach_data"][0]["miss_distance"]["miles"])/238900
           print("Asteroid name: " + asteroid["name"] + " with id of " + asteroid["id"] + " was " + str(num_moonlength) + " away!")


## call main
main()

