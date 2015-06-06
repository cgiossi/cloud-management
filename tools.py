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

def find_highwayid(conn, direction):
    if direction.upper() == 'NORTH':
        domains = find_teamb(conn)
        names = [x.name for x in domains]
        dirDomain = [s for s in names if 'NB' in s][0]
        dom = conn.get_domain(dirDomain)
        query = 'SELECT highwayid FROM `' + dirDomain + '` WHERE direction = "NORTH"'
        results = dom.select(query, max_items=1)
        return results.next()['highwayid']
    elif direction.upper() == 'SOUTH':
        domains = find_teamb(conn)
        names = [x.name for x in domains]
        dirDomain = [s for s in names if 'SB' in s][0]
        dom = conn.get_domain(dirDomain)
        query = 'SELECT highwayid FROM `' + dirDomain + '` WHERE direction = "SOUTH"'
        results = dom.select(query, max_items=1)
        return results.next()['highwayid']
    else:
        print "Not a valid direction"
        return None



