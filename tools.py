import boto.sdb

def find_teamb(conn):
    domains = []
    allDomains = conn.get_all_domains()
    for d in allDomains:
        #Looking for TEAMB in first five characters
        if d.name[0:5] == "TEAMB":
            #Strip TEAMB_ from domain name
            domains += [d]
    return domains

def groupByDetectorid(results):
    detectors = {}
    for i in results:
        try:
            detectors[i['detectorid']] += [float(i['speed'])]
        except KeyError:
            detectors[i['detectorid']] = [float(i['speed'])]
    return detectors
