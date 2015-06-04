import boto.sdb

def find_teamb(conn):
    domains = []
    allDomains = conn.get_all_domains()
    for d in allDomains:
        #Looking for TEAMB in first five characters
        if d.name[0:5] == "TEAMB":
            #Strip TEAMB_ from domain name
            domains += [d]
    return domains
