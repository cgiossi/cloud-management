import boto.sdb
import datetime
import tools

def run(conn, station):
    totalVolume = 0
    dom = conn.get_domain('TEAMB_' + station)
    query = 'SELECT volume FROM `' + dom.name + '` WHERE starttime like "2011-09-21%"'
    print "Querying " + dom.name + " to get the sum of volumes"
    volumes = dom.select(query)
    for v in volumes:
        if v['volume'] != "":
            totalVolume += int(v['volume'])
    return totalVolume
	
