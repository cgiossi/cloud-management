import boto.sdb
import tools
import queryc, queryd, querye, queryff

def call_query(conn):
    #queryff.run(conn)
    results = queryc.run(conn, 'Foster_NB')
    #results = queryd.run(conn, 'TEAMB_Foster_NB')
    #results = querye.run(conn, 3)
    print results

conn = boto.sdb.connect_to_region('us-west-2')
print tools.find_highwayid(conn, 'north')
call_query(conn)
