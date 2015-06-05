import boto.sdb, datetime
import tools

def run(conn, station):
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
        sTime = startTime.strftime('%Y-%m-%d %H:%M:%S-07')
        eTime = endTime.strftime('%Y-%m-%d %H:%M:%S-07')
        query = 'SELECT detectorid, speed, starttime FROM `' + stationDomain.name + '`'
        results = stationDomain.select(query)
        for i in results:
            print i

