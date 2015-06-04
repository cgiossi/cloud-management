import boto.sdb
import queryc

def call_query(conn):
    queryc.run(conn)

conn = boto.sdb.connect_to_region('us-west-2')
call_query(conn)
