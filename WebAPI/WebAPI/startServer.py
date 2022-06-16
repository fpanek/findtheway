#required on Server #!/usr/local/bin/python3.8

from flask import Flask, json
from flask import request
#from WienerLinienAPI.filterStations import stationsWithinRadius
from WienerLinienAPI.filterStations import *
#import WienerLinienAPI.filterStations
from flask_cors import CORS

from WienerLinienAPI.getNearbyStations import saveNearbyStationsIntoFile

#Test Data for stations:
stations = [{"stations": {"station1": {"name": "asdf","distance": "1","stationType": "Bus"},"station2": {"name": "bbbb","distance": "3", "stationType": "train" }, "station3": {"name": "CCCCC","distance": "6",  "stationType": "Bus"	},	"station4": {"name": "DDDDDD",	 "distance": "2","stationType": "ubahn"  } }}]

stationsFile = "stations.json"

api = Flask(__name__)
CORS(api) #TODO WHAT does this line do?...

@api.route('/stations', methods=['GET'])
def get_companies():
  return json.dumps(stations)


def extract_distance(json):
    try:
        return int(json['stations']['distance'])
    except KeyError:
        return 0

@api.route('/getstations', methods=['GET'])
def api_test():
    long = request.args.get('long', default=00.00000)
    lat = request.args.get('lat', default=00.00000)
    rad = request.args.get('rad', default=500)
    valuetoReturn = stationsWithinRadius(stationsFile, float(int(rad)/1000), long, lat)
    myjson = json.dumps(valuetoReturn)
    #print(myjson["stations:"])
    #valuetoReturn.sort(key = extract_distance(valuetoReturn))
    return json.dumps(valuetoReturn)
    #valueToReturn = {"longitude": long, "latitude": lat}
    #return json.dumps(valueToReturn)


#nextbikeAPI: http://nextbike.net/maps/nextbike-official.xml?domains=wr,at
@api.route('/getbikestations', methods=['GET'])
def api_test2():
    long = request.args.get('long', default=00.00000)
    lat = request.args.get('lat', default=00.00000)
    rad = request.args.get('rad', default=500)
    valuetoReturn = stationsWithinRadius(stationsFile, float(int(rad)/1000), long, lat)
    #valuetoReturn = bikeStationsWithinRadius()
    return json.dumps(valuetoReturn)  #dividide by 1000 for meters instead of km
    #valueToReturn = {"longitude": long, "latitude": lat}
    #return json.dumps(valueToReturn)



#Request for locations around actual position:
#https://localhost:$PORT/location?long=45.123213&lat=12.00000&distance=500m

#Request for departure times:
#http://localhost:$PORT/departureTimes?station=XYZ

if __name__ == '__main__':
    saveNearbyStationsIntoFile(stationsFile)    #store stations locally during startup
    api.run()