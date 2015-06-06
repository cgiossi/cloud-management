import boto.sdb

def find_teamb(conn):
    domains = []
    allDomains = conn.get_all_domains()
    for d in allDomains:
        #Looking for TEAMB in first five characters
        if d.name[0:5] == "TEAMB":
            domains += [d]
    return domains

def group_by_detectorid(results):
    detectors = {}
    for i in results:
        try:
            detectors[i['detectorid']] += [float(i['speed'])]
        except KeyError:
            detectors[i['detectorid']] = [float(i['speed'])]
    return detectors

def calculate_travel_time(detectors, stationLength):
    speeds = []
    for key in detectors.keys():
        totalSpeed = sum(detectors[key])
        if len(detectors[key]) != 0:
            averageSpeed = totalSpeed/len(detectors[key])
        speeds += [averageSpeed]
    if len(detectors.keys()) == 0:
        stationSpeed = 0
    else:
        stationSpeed = sum(speeds)/len(detectors.keys())
    if stationSpeed != 0:
        travelTime = (float(stationLength)/stationSpeed) * 3600
    else:
        travelTime = 0
    return travelTime

#def find_highwayid(conn, direction):
