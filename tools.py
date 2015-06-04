import boto.sdb

def strip_teamb(conn):
    domains = []
    allDomains = conn.get_all_domains()
    for d in allDomains:
        #Looking for TEAMB in first five characters
        if d[0:4] == "TEAMB":
            #Strip TEAMB_ from domain name
            domains += [d.strip(6)]
    return domains

