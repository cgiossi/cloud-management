import boto.sdb
import tools


#def run(conn, domains, speed):
def run(args):
	conn = args[0]
	domains = args[1]
	speed = args[2]
	sum = 0
	for station in domains:
		stationDomain = conn.get_domain(station.name)
		query = 'SELECT count(*)  FROM `' + stationDomain.name + '` ' + \
        	'WHERE speed > "' + str(speed) + '" '  
		results = stationDomain.select(query)
		for row in results:
			sum += int(row['Count'])	
	return sum

