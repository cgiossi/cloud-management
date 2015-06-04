import boto.sdb, datetime
import tools

def run(conn):
    stationLengthMapping = {}
    domains = tools.find_teamb(conn)
    #domains is just a list of strings now, so we'll have to grab individual
    #domains through the connection
    for d in domains:
        #Grab domain from sdb to make queries against
        #dom = conn.get_domain(d.name)
        query = 'SELECT direction FROM `' + d.name + '`'
        results = d.select(query, max_items=1)
        #Remove all domains that don't correspond to a NB station
        if results.next()['direction'] != "NORTH":
            print "'Removing southbound domain"
            domains.remove(d)
    startTime = datetime.datetime.strptime("2011-09-22 00:00:00", '%Y-%m-%d %H:%M:%S')
    for domain in domains:
        print "Querying " + domain.name
        query = 'SELECT stationlength FROM `' + domain.name + '`'
        results = domain.select(query, max_items=1)
        for r in results:
            print results
