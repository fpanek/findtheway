import json
from math import radians, cos, sin, asin, sqrt
def dist(lat1, long1, lat2, long2):
    #https://en.wikipedia.org/wiki/Haversine_formula
    # convert decimal degrees to radians
    lat1, long1, lat2, long2 = map(radians, [lat1, long1, lat2, long2])
    # haversine formula
    dlon = long2 - long1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    # Radius of earth in kilometers is 6371
    km = 6371* c
    return km


def stationsWithinRadius(filename, radius,longitude, latitude):
    # Opening JSON file
    with open(filename, 'r') as openfile:
        stations = json.load(openfile)
    result = []
    result.append("stations:")
    for data in stations['features']:
        lat,long = str(data['geometry']['coordinates']).split(',')
        long = str(long).replace(']', '')
        lat = str(lat).replace('[', '')
        distance = dist(float(lat),float(long), float(latitude),float(longitude))
        title = (data['id'])
        stationName = (data['properties']['BEZEICHNUNG'])
        wlNumber = (data['properties']['WL_NUMMER'])
        #TODO - api for station type?..


        if distance <= radius:
            station = {title: {'stationName': stationName, 'distance' : distance, 'stationType' : "TODO", 'wlNumber' : wlNumber}}
            result.append(station)



    #test = json.dumps(result)
    #print(test)
    return (result)


def teeeest:
    return "halloe"

def bikeStationsWithinRadius(filename, radius,longitude, latitude):
    # Opening JSON file
    with open(filename, 'r') as openfile:
        stations = json.load(openfile)
    result = []
    result.append("stations:")
    for data in stations['features']:
        lat,long = str(data['geometry']['coordinates']).split(',')
        long = str(long).replace(']', '')
        lat = str(lat).replace('[', '')
        distance = dist(float(lat),float(long), float(latitude),float(longitude))
        title = (data['id'])
        stationName = (data['properties']['BEZEICHNUNG'])
        wlNumber = (data['properties']['WL_NUMMER'])
        #TODO - api for station type?..
    return ("asdf")