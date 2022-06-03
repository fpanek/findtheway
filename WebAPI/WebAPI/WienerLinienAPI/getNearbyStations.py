#!/usr/bin/python3
#retrieve next locations from the Wiener Linien API
import json
import requests

stationsApiURL = "https://data.wien.gv.at/daten/geo?service=WFS&request=GetFeature&version=1.1.0&typeName=ogdwien:HALTESTELLEWLOGD&srsName=EPSG:4326&outputFormat=json"

def saveNearbyStationsIntoFile(filename):
    response = requests.get(stationsApiURL).json()
    #stations = open(filename, "w+")
    with open(filename, "w") as outfile:
        #outfile.write(response.text)
        json.dump(response,outfile)
    #stationen.write(response.text)
    #stations.close()

