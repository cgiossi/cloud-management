import boto.sdb
import tools
import querya, queryb, queryc, queryd, querye, queryf

def call_query(conn, query, args=[]):
    domainPrefix = 'TEAMB_'
    if query == 'A':
        domains = tools.find_teamb(conn)
        speed = 100
        if len(args) != 0:
            speed = args[0]
        results = querya.run(conn, domains, speed)
    elif query == 'B':
        station = domainPrefix + 'Foster_NB'
        if len(args) != 0:
            station = domainPrefix + args[0]
        results = queryb.run(conn, station)
    elif query == 'C':
        station = domainPrefix + 'Foster_NB'
        date = '2011-09-22'
        if len(args) != 0:
            station = domainPrefix + args[0]
        if len(args) >= 2:
            date = args[1]
        results = queryc.run(conn, station, date)
    elif query == 'D':
        station = domainPrefix + 'Foster_NB'
        date = '2011-09-22'
        if len(args) != 0:
            station = domainPrefix + args[0]
        if len(args) >= 2:
            date = args[1]
        results = queryd.run(conn, station, date)
    elif query == 'E':
        highwayid = 3
        date = '2011-09-22'
        if len(args) != 0:
            highwayid = args[0]
        if len(args) >= 2:
            date = args[1]
        results = querye.run(conn, highwayid, date)
    elif query == 'F':
        results = queryf.run(conn)
    else:
        results =  "Invalid query"
    print results

def main():
    region = 'us-west-2'
    print "Connecting to simpleDB"
    conn = boto.sdb.connect_to_region(region)
    if conn == None:
        print "Could not connect to region"
        exit()
    print "Connected to " + region
    #print tools.find_highwayid(conn, 'north')
    print "Enter a query to run, or type EXIT to quit"
    query = raw_input('Enter the query you wish to run: ')
    while (query.upper() != "EXIT"):
        call_query(conn, query.upper())
        query = raw_input('Enter the query you wish to run: ')

if __name__ == "__main__":
    main()
