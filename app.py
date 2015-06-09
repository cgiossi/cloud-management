import boto.sdb
import os
import tools
import querya, queryb, queryc, queryd, querye, queryf

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    TEST = '\033[101m'


def call_query(conn, query, args=[]):
    domainPrefix = 'TEAMB_'
    if query == 'A':
        domains = tools.find_teamb(conn)
        speed = 100
        if len(args) != 0:
            speed = args[0]
        runTime, results = tools.run_time(querya.run, [conn, domains, speed])
        print runTime
    elif query == 'B':
        station = domainPrefix + 'Foster_NB'
        if len(args) != 0:
            station = domainPrefix + args[0]
        runTime, results = tools.run_time(queryb.run, [conn, station])
    elif query == 'C':
        station = domainPrefix + 'Foster_NB'
        date = '2011-09-22'
        if len(args) != 0:
            station = domainPrefix + args[0]
        if len(args) >= 2:
            date = args[1]
        runTime, results = tools.run_time(queryc.run, [conn, station, date])
    elif query == 'D':
        station = domainPrefix + 'Foster_NB'
        date = '2011-09-22'
        if len(args) != 0:
            station = domainPrefix + args[0]
        if len(args) >= 2:
            date = args[1]
        runTime, results = tools.run_time(queryd.run, [conn, station, date])
    elif query == 'E':
        highwayid = 3
        date = '2011-09-22'
        if len(args) != 0:
            highwayid = args[0]
        if len(args) >= 2:
            date = args[1]
        runTime, results = tools.run_time(querye.run, [conn, highwayid, date])
    elif query == 'F':
        runTime, results = tools.run_time(queryf.run, [conn])
    else:
        results = bcolors.TEST + "Invalid query" + bcolors.ENDC
    print results
    print "Query " + query.upper() + " took " + str(runTime) + " seconds to execute."

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    region = 'us-west-2'
    print bcolors.HEADER + "Connecting to simpleDB" + bcolors.ENDC
    conn = boto.sdb.connect_to_region(region)
    if conn == None:
        print bcolors.FAIL + "Could not connect to region" + bcolors.ENDC
        exit()
    print bcolors.OKGREEN + "Connected to " + region + bcolors.ENDC
    #print tools.find_highwayid(conn, 'north')
    print "Enter a query to run, or type EXIT to quit"
    prompt = bcolors.WARNING + \
             'Enter the query you wish to run followed by any arguments you would like to include \n' + \
             'For example: c Foster_NB 2011-09-22\n' + bcolors.ENDC
    userInput = ''
    while (True):
        userInput = raw_input(prompt)
        if userInput.upper() == 'EXIT':
            break
        args = userInput.split(' ')[1:]
        query = userInput.split(' ')[0]
        call_query(conn, query.upper(), args)
        raw_input('Press enter to continue...')
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
