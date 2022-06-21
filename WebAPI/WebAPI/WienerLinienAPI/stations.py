#required on Server #!/usr/local/bin/python3.8

from flask import Blueprint, render_template, request, flash, redirect
from flask import Flask, make_response
from WienerLinienAPI.filterStations import *
from WienerLinienAPI.getNearbyStations import *
from userManagement.models import User
from userManagement.auth import isloggedin
from flask import jsonify

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
@isloggedin
def api_test():
    long = request.args.get('long', default=00.00000)
    lat = request.args.get('lat', default=00.00000)
    rad = request.args.get('rad', default=500)
    valuetoReturn = stationsWithinRadius(stationsFile, float(int(rad)/1000), long, lat, stationsStopIDFile)
    cookie = request.cookies.get('id')
    email = request.cookies.get('email')
    user = User.query.filter_by(email=email).first()
    #print(cookie)
    #print(email)
    #print(user.cookieID)
    if user:
        if user.cookieID == cookie:
        #if 1==1:
            print("Meine cookie id ist: ")
            print(cookie)
            response = make_response(json.dumps(valuetoReturn))
            #response = jsonify(success=False, responseText="correct login data", id ="xyz")
            response.headers.add('Access-Control-Allow-Origin', 'https://findtheway.geokhugo.com:1234')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response
        else:
            response = jsonify(success=False, responseText="cookie not equal", id ="xyz")
            response.status_code = 400
            response.set_cookie("sdfasdf", "asdf") 
            response.headers.add('Access-Control-Allow-Origin', 'https://findtheway.geokhugo.com:1234')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response
    else:
        response = jsonify(success=False, responseText="wrong login data", id ="xyz")
        response.status_code = 400
        response.set_cookie("sdfasdf", "asdf") 
        response.headers.add('Access-Control-Allow-Origin', 'https://findtheway.geokhugo.com:1234')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        return response
    #return json.dumps(valuetoReturn)
    #valueToReturn = {"longitude": long, "latitude": lat}
    #return json.dumps(valueToReturn)
    response = jsonify(success=False, responseText="elif NOK", id ="xyz")
    response.status_code = 400
    response.set_cookie("sdfasdf", "asdf") 
    response.headers.add('Access-Control-Allow-Origin', 'https://findtheway.geokhugo.com:1234')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response


#nextbikeAPI: http://nextbike.net/maps/nextbike-official.xml?domains=wr,at
@stations.route('/getbikestations', methods=['GET'])
@isloggedin
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
