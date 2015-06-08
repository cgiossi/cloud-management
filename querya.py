import boto.sdb
import tools


def run(conn,domains, speed):

	for station in domains:
		stationDomain = conn.get_domain( station.name)
		query = 'SELECT count(*)  FROM `' + stationDomain.name + '` ' + \
        	'WHERE speed > "' + str(speed) + '" '  
		results = stationDomain.select(query, max_items=1)
		for row in results:
			sum += int(row['Count'])	
	return sum

