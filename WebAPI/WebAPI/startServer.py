#required on Server #!/usr/local/bin/python3.8

#General documenation of API https://www.wienerlinien.at/ogd_realtime/doku/ogd/wienerlinien-echtzeitdaten-dokumentation.pdf
#TODO Abfahrtszeiten Request
#TODO order list distance ascending
#TODO type of station ausgeben, meherer auf einmal
#TODO enhance json with long lat for google maps

from flask import Flask, json
from flask import request
from WienerLinienAPI.filterStations import *
from flask_cors import CORS
import json

from userManagement import create_app

from WienerLinienAPI.getNearbyStations import *



#api = Flask(__name__)
app = create_app()
#CORS(api) #TODO WHAT does this line do?...

if __name__ == '__main__':
    #saveNearbyStationsIntoFile(stationsFile, stationsStopIDFile)    #store stations locally during startup
    #saveNearbyStationsStopIDIntoFile(stationsStopIDFile)
    app.run(host='0.0.0.0', port='4999')