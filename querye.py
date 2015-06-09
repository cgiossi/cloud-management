import boto.sdb
import tools
import queryd

def run(args):
    conn = args[0]
    highwayid = args[1]
    date = args[2]
    domains = tools.find_teamb(conn)
    results = []
    for domain in domains:
        #print domain.name
        query = 'SELECT highwayid FROM `' + domain.name + '`'
        hid = domain.select(query, max_items=1)
        if int(hid.next()['highwayid']) == highwayid:
            results += [queryd.run([conn, domain.name, date])]
    morningTravelTime = []
    eveningTravelTime = []
    for tt in results:
        if tt[0] != "" and tt[0] != 0:
            morningTravelTime += [tt[0]]
        if tt[1] != "" and tt[1] != 0:
            eveningTravelTime += [tt[1]]
    avgMorningTravelTime = sum(morningTravelTime)/60
    avgEveningTravelTime = sum(eveningTravelTime)/60
    totalTravelTime = (avgMorningTravelTime, avgEveningTravelTime)
    return totalTravelTime
