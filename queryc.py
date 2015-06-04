import boto.sdb
import tools.py as tools

def run(conn):
    stationLengthMapping = {}
    domains = tools.strip_teamb(conn)
    for domain in domains:
        query = 'SELECT direction FROM `' + domain.name + '` LIMIT "1"'
        results = domain.select(query)
        #Remove all domains that don't correspond to a NB station
        if results[0] != "NB":
            domains.remove(domain)
    for domain in domain:
        query = 'SELECT detectorid, starttime, speed FROM `' + domain.name + \
                '` WHERE speed > "0" AND starttime LIKE "2011-09-21%"'
        query = 'SELECT stationlength FROM `' + domain.name + \
                        '` LIMIT "1"'
        
