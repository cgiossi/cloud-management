import boto.sdb


conn = boto.sdb.connect_to_region('us-west-2')
print conn
rs1 = []
domains = []
route =[]
allDomains = conn.get_all_domains()
for d in allDomains:
	#Looking for TEAMB in first five characters
	if d.name[0:5] == "TEAMB":
            #Strip TEAMB_ from domain name
		domains += [d]

for dom in domains:
	query = 'SELECT locationtext,stationid,downstream,upstream FROM `' + dom.name + '`'
	rs =dom.select(query,max_items=1)
	rs1 += rs
#for j in rs1:
#	print j
for row in rs1:
	if row['locationtext'] == 'Johnson Cr NB':
		did = row['downstream']
#		print did
	if row['locationtext'] == 'I-205 NB at Columbia':
		uid = row['upstream']
		print uid

while (did != uid):
	for row in rs1:
	#print row['stationid']
		if (row['stationid'] == did):
			route += [str(row['locationtext'])]
			did = row['downstream']
			break

print route