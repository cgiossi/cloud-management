import boto.sdb
import datetime
import tools

def runqueryb(con, dom)
	totalVolume = 0
	dom = conn.get_domain(‘TEAMB_’ + station)
	query = ‘SELECT volume FROM `’ + dom.name + ‘` WHERE starttime like “2011-09-21%”’
	volumes = dom.select(query, max_items=1)
	print “Quering” + dom.name + “ to get the sum of volumes”
	for v in volumes:
			totalVolume += int(v[‘volume’])
	return totalVolume
	
