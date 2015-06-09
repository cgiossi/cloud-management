import boto.sdb, datetime
import tools

def run(args):
    conn = args[0]
    station = args[1]
    date = args[2]
    count = 0
    retResults = []
    timeInterval = datetime.timedelta(0,0,0,0,5)
    startTime = datetime.datetime.strptime(date + " 00:00:00", '%Y-%m-%d %H:%M:%S')
    endTime = datetime.datetime.strptime(date + " 00:05:00", '%Y-%m-%d %H:%M:%S')
    print startTime.strftime('%Y-%m-%d %H:%M:%S')

    stationDomain = conn.get_domain(station)

    print "Querying " + stationDomain.name + " for station length"
    query = 'SELECT length FROM `' + stationDomain.name + '`'
    results = stationDomain.select(query, max_items=1)
    stationLength = results.next()['length']
    nextDay = startTime + datetime.timedelta(1)

    while startTime < nextDay:
        sTime = startTime.strftime('%Y-%m-%d %H:%M:%S')
        eTime = endTime.strftime('%Y-%m-%d %H:%M:%S')
        query = 'SELECT detectorid, speed, starttime FROM `' + stationDomain.name + '` ' + \
                'WHERE starttime < "' + eTime + '" ' + \
                'AND starttime > "' + sTime + '" ' + \
                'AND speed != "" ' + \
                'AND speed > "0" ' + \
                'ORDER BY starttime'
        results = stationDomain.select(query)
        detectors = tools.group_by_detectorid(results)
        startTime += timeInterval
        endTime += timeInterval
        travelTime = tools.calculate_travel_time(detectors, stationLength)
        count += 1
        retResults += [travelTime]
    return retResults
