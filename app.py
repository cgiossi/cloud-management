import boto.sdb
import os
import tools
import querya, queryb, queryc, queryd, querye, queryf

class bcolors:
    BRIGHTWHITE = '\x1b[37m'
    DARKCYAN = '\x1b[36;1m'
    DARKMAGENTA = '\x1b[35;1m'
    DARKYELLOW = '\x1b[33;1m'
    HEADER = '\033[95m'
    OKCYAN = '\033[96m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def call_query(conn, query, args=[]):
    domainPrefix = 'TEAMB_'
    if query == 'A':
        domains = tools.find_teamb(conn)
        speed = 100
        if len(args) != 0:
            speed = args[0]
        runTime, results = tools.run_time(querya.run, [conn, domains, speed])
    elif query == 'B':
        station = domainPrefix + 'Foster_NB'
        date = '2011-09-21'
        if len(args) != 0:
            station = domainPrefix + args[0]
        if len(args) >= 2:
            date = args[1]
        runTime, results = tools.run_time(queryb.run, [conn, station, date])
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
	print "\nAverage Travel Time in Morning\t Average Travel Time in Evening"
        runTime, results = tools.run_time(queryd.run, [conn, station, date])
    elif query == 'E':
        highwayid = 3
        date = '2011-09-22'
        if len(args) != 0:
            if len(args[0]) == 1:
                if args[0] != '3' and args[0] != '4':
                    print "Invalid highwayid"
                    return
                highwayid = args[0]
            else:
                highwayid = int(tools.find_highwayid(conn, args[0]))
                if highwayid == None:
                    print args[0] + " is an invalid direction"
                    return
                print "Corresponding highwayid is " + str(highwayid)
        if len(args) >= 2:
            date = args[1]
        runTime, results = tools.run_time(querye.run, [conn, highwayid, date])
    elif query == 'F':
        runTime, results = tools.run_time(queryf.run, [conn])
    else:
        results = bcolors.FAIL + "Invalid query" + bcolors.ENDC
        print results
        return
    if query=='C':
    	print ' '.join(results)
    elif results == None:
        return
    else:
        print results
    print "\nQuery " + query.upper() + " took " + str(runTime) + " seconds to execute.\n"

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    region = 'us-west-2'
    print bcolors.HEADER + "Connecting to simpleDB" + bcolors.ENDC
    conn = boto.sdb.connect_to_region(region)
    if conn == None:
        print bcolors.FAIL + "Could not connect to region" + bcolors.ENDC
        exit()
    print bcolors.OKGREEN + "Connected to " + region + bcolors.ENDC
    print bcolors.DARKYELLOW + "Enter a query to run, or type EXIT to quit" + bcolors.ENDC
    prompt = bcolors.DARKYELLOW + \
             'Enter the query you wish to run followed by any arguments you would like to include \n' + \
             'For example: c Foster_NB 2011-09-22\n' + \
             'Enter \'help\' for the queries and syntax that can be run\n' + bcolors.ENDC
    userInput = ''
    while (True):
        userInput = raw_input(prompt)
        if userInput.upper() == 'EXIT' or userInput.upper() == 'Q':
            break
        elif userInput.upper() == 'HELP':
            os.system('cls' if os.name == 'nt' else 'clear')
            tools.help()
        else:
            args = userInput.split(' ')[1:]
            query = userInput.split(' ')[0]
            call_query(conn, query.upper(), args)
        raw_input('Press enter to continue...')
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
