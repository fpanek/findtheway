#required on Server #!/usr/local/bin/python3.8

from flask import Flask, json
from flask import request
import requests
from WienerLinienAPI.getNearbyStations import saveNearbyStationsIntoFile
#from WienerLinienAPI.filterStations import stationsWithinRadius
import WienerLinienAPI.getNearbyStations
from flask_cors import CORS

#Test Data for stations:
stations = [{"stations": {"station1": {"name": "asdf","distance": "1","stationType": "Bus"},"station2": {"name": "bbbb","distance": "3", "stationType": "train" }, "station3": {"name": "CCCCC","distance": "6",  "stationType": "Bus"	},	"station4": {"name": "DDDDDD",	 "distance": "2","stationType": "ubahn"  } }}]

stationsFile = "stations.json"

api = Flask(__name__)
CORS(api) #TODO WHAT does this line do?...

@api.route('/stations', methods=['GET'])
def get_companies():
  return json.dumps(stations)

@api.route('/getstations', methods=['GET'])
def api_test():
    long = request.args.get('long', default=00.00000)
    lat = request.args.get('lat', default=00.00000)
    rad = request.args.get('rad', default=500)
    valuetoReturn = stationsWithinRadius(stationsFile, float(int(rad)/1000), long, lat)
    return json.dumps(valuetoReturn)  #dividide by 1000 for meters instead of km
    #valueToReturn = {"longitude": long, "latitude": lat}
    #return json.dumps(valueToReturn)


#nextbikeAPI: http://nextbike.net/maps/nextbike-official.xml?domains=wr,at
@api.route('/getbikestations', methods=['GET'])
def api_test():
    long = request.args.get('long', default=00.00000)
    lat = request.args.get('lat', default=00.00000)
    rad = request.args.get('rad', default=500)
    #valuetoReturn = stationsWithinRadius(stationsFile, float(int(rad)/1000), long, lat)
    valuetoReturn =
    return json.dumps(valuetoReturn)  #dividide by 1000 for meters instead of km
    #valueToReturn = {"longitude": long, "latitude": lat}
    #return json.dumps(valueToReturn)



#Request for locations around actual position:
#https://localhost:$PORT/location?long=45.123213&lat=12.00000&distance=500m

#Request for departure times:
#http://localhost:$PORT/departureTimes?station=XYZ

if __name__ == '__main__':
    saveNearbyStationsIntoFile(stationsFile)    #store stations locally during startup
    api.run(host='0.0.0.0')