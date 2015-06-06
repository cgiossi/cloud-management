import boto.sdb
import datetime
import tools

def runqueryb(conn, station):
    totalVolume = 0
    dom = conn.get_domain('TEAMB_' + station)
    query = 'SELECT volume FROM `' + dom.name + '` WHERE starttime like "2011-09-21%"'
    print "Quering " + dom.name + " to get the sum of volumes"
    volumes = dom.select(query)
    for v in volumes:
        if v['volume'] != "":
            totalVolume += int(v['volume'])
    return totalVolume
	
