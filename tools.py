import boto.sdb
import time


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

def run_time(query, args):
    start = time.time()
    results = query(args)
    end = time.time()
    return end - start, results

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    TEST = '\033[101m'

def help():
    print bcolors.OKGREEN,
    print "\ba",
    print bcolors.ENDC
    print bcolors.OKBLUE,
    print "\bFind the count of vehicles travelling greater than 100 MPH",
    print bcolors.ENDC
    print bcolors.OKGREEN,
    print "\bb [station]",
    print bcolors.ENDC
    print bcolors.OKBLUE,
    print "\bFind the volume of a given station on a given date. Defaults to Foster_NB and"
    print "2011-09-21. Dates should be of the form YYYY-MM-DD.",
    print bcolors.ENDC
    print bcolors.OKGREEN,
    print "\bc [station] [date]",
    print bcolors.ENDC
    print bcolors.OKBLUE,
    print "\bFind the travel time for five minute intervals of the given stations and given"
    print "date. Defaults to Foster_NB and 2011-09-22. Dates should of the form YYYY-MM-DD",
    print bcolors.ENDC
    print bcolors.OKGREEN,
    print "\bd [station] [date]",
    print bcolors.ENDC
    print bcolors.OKBLUE,
    print "\bFind the travel time for peak periods of the given stations on the given date."
    print "Results are in seconds. Defaults to Foster_NB and 2011-09-22. Dates should be"
    print "of the form YYYY-MM-DD.",
    print bcolors.ENDC
    print bcolors.OKGREEN,
    print "\be ([highwayid]|[direction]) [date]",
    print bcolors.ENDC
    print bcolors.OKBLUE,
    print "\bFind the travel time for peak periods of the given highway on the given date."
    print "Results arae in minutes. Defaults to I-205 NB and 2011-09-22. Currently only"
    print "supports I-205. Direction should be either north or south. Dates should be of"
    print "the form YYYY-MM-DD.",
    print bcolors.ENDC
    print bcolors.OKGREEN,
    print "\bf",
    print bcolors.ENDC
    print bcolors.OKBLUE,
    print "\bFind a route from Johnson Cr Blvd and I-205 NB at Columbia"
    print bcolors.ENDC
