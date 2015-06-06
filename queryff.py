import boto.sdb
import tools 

def run(conn):
	stationLengthMapping = {}
	domains = tools.find_teamb(conn)
	for d in domains:
     		query = 'SELECT direction FROM `' + d.name + '`'
     		results = d.select(query, max_items=1)
      #Remove all domains that don't correspond to a NB station
      	if results.next()['direction'] != "NORTH":
           	print "Removing southbound domain from domains to query"
            	domains.remove(d)
	for dom in domains:
		query = 'SELECT locationtext,stationid,downstream,upstream FROM `' + dom.name + '`'
		rs1 =dom.select(query)
	for row in rs1:
		if row['locationnext'] == 'Johnson Creek SB':
			did = row['downstreamid']
		if row['locationnext'] == 'Columbia to I-205 NB':
			uid = row['upstreamid']
	while (did <> uid):
		for row in rs1:
			if row['stationid'] == did:
				route = + row.next()['locationnext']
				did = row['downstreamid']

 
	print route