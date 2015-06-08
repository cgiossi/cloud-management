import boto.sdb
import tools
import queryc, queryd, querye, queryff

def call_query(conn, query):
    if query == 'A'
        querya.run(conn)
    if query == 'B'
        queryb.run(conn)
    if query == 'C'
        queryc.run(conn)
    if query == 'D'
        queryd.run(conn)
    if query == 'E'
        querye.run(conn)
    if query == 'F'
        queryf.run(conn)
    #queryff.run(conn)
    results = queryc.run(conn, 'Foster_NB')
    #results = queryd.run(conn, 'TEAMB_Foster_NB')
    #results = querye.run(conn, 3)
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
    query = raw_input('Enter the query you wish to run: ')
    call_query(conn, query.upper())
