#required on Server #!/usr/local/bin/python3.8

from flask import Blueprint, render_template, request, flash, redirect

from WienerLinienAPI.filterStations import *
from WienerLinienAPI.getNearbyStations import *


#Test Data for stations:
stations = [{"stations": {"station1": {"name": "asdf","distance": "1","stationType": "Bus"},"station2": {"name": "bbbb","distance": "3", "stationType": "train" }, "station3": {"name": "CCCCC","distance": "6",  "stationType": "Bus"	},	"station4": {"name": "DDDDDD",	 "distance": "2","stationType": "ubahn"  } }}]

stationsFile = "stations.json"
stationsStopIDFile = "stations_stopID.csv"

#api = Flask(__name__)
#app = create_app()
#CORS(api) #TODO WHAT does this line do?...


stations = Blueprint('stations', __name__)

def extract_distance(json):
    try:
        return int(json['distance'])
    except KeyError:
        return 0

@stations.route('/getstations', methods=['GET'])
def api_test():
    long = request.args.get('long', default=00.00000)
    lat = request.args.get('lat', default=00.00000)
    rad = request.args.get('rad', default=500)
    valuetoReturn = stationsWithinRadius(stationsFile, float(int(rad)/1000), long, lat, stationsStopIDFile)
    return json.dumps(valuetoReturn)
    #valueToReturn = {"longitude": long, "latitude": lat}
    #return json.dumps(valueToReturn)


#nextbikeAPI: http://nextbike.net/maps/nextbike-official.xml?domains=wr,at
@stations.route('/getbikestations', methods=['GET'])
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
    #saveNearbyStationsIntoFile(stationsFile, stationsStopIDFile)    #store stations locally during startup
    saveNearbyStationsStopIDIntoFile(stationsStopIDFile)
    api.run(host='0.0.0.0', port='4999')