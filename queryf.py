import boto.sdb
import tools


def run(args):
	conn = args[0]
	rs1 = []
	#domains = []
	route =[]
	flag='Y'
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
			#print uid
	#if the downstream id and upstream id are null then route cannot be found
	if (did==None) or (uid == None):
		print "Error! Route cannot be found"
	else:
		while (did != uid):
			for row in rs1:
				if (row['stationid'] == did):
					#print row['stationid']
					route += [str(row['locationtext'])]
					did = row['downstream']
					break
			if (did == '0') and (did!=uid):
				route= "No direct Route between the stations"
				flag='N'
				break
		if(flag=='Y'):
			route += [str(finalLocation)]
		return route
