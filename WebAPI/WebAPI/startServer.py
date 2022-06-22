#!/usr/local/bin/python3.8

#General documenation of API https://www.wienerlinien.at/ogd_realtime/doku/ogd/wienerlinien-echtzeitdaten-dokumentation.pdf
#TODO Abfahrtszeiten Request

from flask import Flask, json
from flask import request
from WienerLinienAPI.filterStations import *
from flask_cors import CORS
import json

from userManagement import create_app

from WienerLinienAPI.getNearbyStations import *

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='4999')
