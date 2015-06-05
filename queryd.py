import boto.sdb, datetime
import tools

def run(conn):
    stationLengthMapping = {}
    timeInterval = datetime.timedelta(0,0,0,0,5)
    domains = tools.find_teamb(conn)
    #domains is just a list of strings now, so we'll have to grab individual
    #domains through the connection
    for d in domains:
        #Grab domain from sdb to make queries against
        query = 'SELECT direction FROM `' + d.name + '`'
        results = d.select(query, max_items=1)
        #Remove all domains that don't correspond to a NB station
        if results.next()['direction'] != "NORTH":
            print "Removing southbound domain from domains to query"
            domains.remove(d)
    for domain in domains:
        print "Querying " + domain.name
        query = 'SELECT stationlength FROM `' + domain.name + '`'
        results = domain.select(query, max_items=1)
    startTime = datetime.datetime.strptime("2011-09-22 00:00:00", '%Y-%m-%d %H:%M:%S')
    endTime = datetime.datetime.strptime("2011-09-22 00:05:00", '%Y-%m-%d %H:%M:%S')
    while startTime < datetime.strptime("2011-09-23 00:00:00", '%Y-%m-%d %H:%M:%S'):
        query = 'SELECT speed FROM `' + domain.name +'` WHERE starttime between "' + \
                startTime.strftime('%Y-%m-%d %H:%M:%s') + '" AND "' + \
                endTime.strftime('%Y-%m-%d %H:%M:%s') + '"'
        
