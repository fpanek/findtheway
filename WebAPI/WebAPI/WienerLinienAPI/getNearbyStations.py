#!/usr/bin/python3
#retrieve next locations from the Wiener Linien API
import json
import time

import requests
import csv

stationsApiURL = "https://data.wien.gv.at/daten/geo?service=WFS&request=GetFeature&version=1.1.0&typeName=ogdwien:HALTESTELLEWLOGD&srsName=EPSG:4326&outputFormat=json"


stationStopID = "http://www.wienerlinien.at/ogd_realtime/doku/ogd/wienerlinien-ogd-haltepunkte.csv"
StationInformation = "https://www.wienerlinien.at/ogd_realtime/monitor?diva="


def saveNearbyStationsIntoFile(filename, stopFile):
    response = requests.get(stationsApiURL).json()
    with open(filename, "w") as outfile:
        json.dump(response,outfile)



    for x in response['features']:
        stationName = (x['properties']['BEZEICHNUNG'])
        stationType = []
        if stationName != "":
            with open(stopFile, 'r') as file:
                reader = csv.reader(file, delimiter=";")
                for row in reader:
                    # print(row[2])
                    if row[2].startswith(stationName):
                        diva = row[1] ##diva number of the station
                        if diva:
                            stationTypeResponse = requests.get( "https://www.wienerlinien.at/ogd_realtime/monitor?diva=" + diva).json()
                            #print (stationTypeResponse['data'][''])
                            print(stationTypeResponse)
                            time.sleep(5)






def saveNearbyStationsStopIDIntoFile(filename):
    print("requestinf file...")
    response = requests.get(stationStopID).content
    csv_file = open(filename, 'wb')
    csv_file.write(response)
    csv_file.close()

