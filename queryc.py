import boto.sdb, datetime
import tools

def groupByDetectorid(results):
    detectors = {}
    for i in results:
        try:
            detectors[i['detectorid']] += [float(i['speed'])]
        except KeyError:
            detectors[i['detectorid']] = [float(i['speed'])]
    return detectors

def run(conn, station):
    count = 0
    timeInterval = datetime.timedelta(0,0,0,0,5)
    startTime = datetime.datetime.strptime("2011-09-22 00:00:00", '%Y-%m-%d %H:%M:%S')
    endTime = datetime.datetime.strptime("2011-09-22 00:05:00", '%Y-%m-%d %H:%M:%S')
    print startTime.strftime('%Y-%m-%d %H:%M:%S')

    stationDomain = conn.get_domain('TEAMB_' + station)

    query = 'SELECT direction FROM `' + stationDomain.name + '`'
    results = stationDomain.select(query, max_items=1)

    print "Querying " + stationDomain.name + " for station length"
    query = 'SELECT length FROM `' + stationDomain.name + '`'
    results = stationDomain.select(query, max_items=1)
    stationLength = results.next()['length']

    while startTime < datetime.datetime.strptime("2011-09-23 00:00:00", '%Y-%m-%d %H:%M:%S'):
        sTime = startTime.strftime('%Y-%m-%d %H:%M:%S')
        eTime = endTime.strftime('%Y-%m-%d %H:%M:%S')
        query = 'SELECT detectorid, speed, starttime FROM `' + stationDomain.name + '` ' + \
                'WHERE starttime < "' + eTime + '" ' + \
                'AND starttime > "' + sTime + '" ' + \
                'AND speed != "" ' + \
                'ORDER BY starttime'
        results = stationDomain.select(query)
        detectors = groupByDetectorid(results)
        startTime += timeInterval
        endTime += timeInterval
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
        count += 1
        print str(travelTime) + ' ' + str(count)
