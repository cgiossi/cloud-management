import boto.sdb
import tools


def run(conn):
	rs1 = []
	domains = []
	route =[]
	domains = tools.find_teamb(conn)

	for dom in domains:
		query = 'SELECT locationtext,stationid,downstream,upstream FROM `' + dom.name + '`'
		rs = dom.select(query,max_items=1)
		rs1 += rs
	for row in rs1:
		if row['locationtext'] == 'Johnson Cr NB':
			did = row['downstream']
			route += [str(row['locationtext'])]
		if row['locationtext'] == 'I-205 NB at Columbia':
			uid = row['stationid']
			finalLocation = row['locationtext']
			print uid

	while (did != uid):
		for row in rs1:
			if (row['stationid'] == did):
				print row['stationid']
				route += [str(row['locationtext'])]
				did = row['downstream']
				break
	route += [str(finalLocation)]
	return route
