import boto.sdb
import tools

#Find travel time for 7-9AM and 4-6PM 9/22/11 in seconds for Foster NB
def run(args):
    conn = args[0]
    station = args[1]
    date = args[2]
    morningStartTime = date + " 07:00:00"
    morningEndTime = date + " 09:00:00"
    eveningStartTime = date + " 16:00:00"
    eveningEndTime = date + " 18:00:00"
    
    print station
    print "\nAvg TT in Morning\tAvg TT in Evening\n"
    domain = conn.get_domain(station)
    
    query = 'SELECT length FROM `' + domain.name + '`'
    results = domain.select(query, max_items=1)
    stationLength = results.next()['length']

    query = 'SELECT detectorid, speed, starttime ' + \
            'FROM `' + domain.name + '`' + \
            'WHERE starttime >= "' + morningStartTime + '" ' + \
            'AND starttime < "' + morningEndTime + '" ' + \
            'AND speed > "0" ' + \
            'AND speed != ""'

    results = domain.select(query)
    groupedSpeeds = tools.group_by_detectorid(results)
    morningTravelTime = tools.calculate_travel_time(groupedSpeeds, stationLength)

    query = 'SELECT detectorid, speed, starttime ' + \
            'FROM `' + domain.name + '`' + \
            'WHERE starttime >= "' + eveningStartTime + '" ' + \
            'AND starttime < "' + eveningEndTime + '" ' + \
            'AND speed > "0" ' + \
            'AND speed != ""'

    results = domain.select(query)
    groupedSpeeds = tools.group_by_detectorid(results)
    eveningTravelTime = tools.calculate_travel_time(groupedSpeeds, stationLength)

    return (morningTravelTime, eveningTravelTime)
