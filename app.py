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

def help():
    print bcolors.OKGREEN,
    print "\ba [speed]",
    print bcolors.ENDC
    print bcolors.OKBLUE,
    print "\bFind the count of vehicles travelling greater than speed. Defaults to 100 MPH",
    print bcolors.ENDC
    print bcolors.OKGREEN,
    print "\bb [station]",
    print bcolors.ENDC
    print bcolors.OKBLUE,
    print "\bFind the volume of a given station on a given date. Defaults to Foster_NB and"
    print "2011-09-21. Dates should be of the form YYYY-MM-DD.",
    print bcolors.ENDC
    print bcolors.OKGREEN,
    print "\bc [station] [date]",
    print bcolors.ENDC
    print bcolors.OKBLUE,
    print "\bFind the travel time for five minute intervals of the given stations and given"
    print "date. Defaults to Foster_NB and 2011-09-22. Dates should of the form YYYY-MM-DD",
    print bcolors.ENDC
    print bcolors.OKGREEN,
    print "\bd [station] [date]",
    print bcolors.ENDC
    print bcolors.OKBLUE,
    print "\bFind the travel time for peak periods of the given stations on the given date."
    print "Results are in seconds. Defaults to Foster_NB and 2011-09-22. Dates should be"
    print "of the form YYYY-MM-DD.",
    print bcolors.ENDC
    print bcolors.OKGREEN,
    print "\be ([highwayid]|[direction]) [date]",
    print bcolors.ENDC
    print bcolors.OKBLUE,
    print "\bFind the travel time for peak periods of the given highway on the given date."
    print "Results arae in minutes. Defaults to I-205 NB and 2011-09-22. Currently only"
    print "supports I-205. Direction should be either north or south. Dates should be of"
    print "the form YYYY-MM-DD.",
    print bcolors.ENDC
    print bcolors.OKGREEN,
    print "\bf",
    print bcolors.ENDC
    print bcolors.OKBLUE,
    print "\bFind a route from Johnson Cr Blvd and I-205 NB at Columbia"
    print bcolors.ENDC
    

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
                if args[0] != 3 or args[0] != 4:
                    print "Invalid highwayid"
                    return
                highwayid = args[0]
            else:
                highwayid = find_highwayid(conn, args[0])
                if highwayid == None:
                    print args[0] + " is an invalid direction"
                    return
        if len(args) >= 2:
            date = args[1]
        runTime, results = tools.run_time(querye.run, [conn, highwayid, date])
    elif query == 'F':
        runTime, results = tools.run_time(queryf.run, [conn])
    else:
        results = bcolors.TEST + "Invalid query" + bcolors.ENDC
        print results
        return
    if query=='C':
    	print ' '.join(results)
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
    #print tools.find_highwayid(conn, 'north')
    print "Enter a query to run, or type EXIT to quit"
    prompt = bcolors.WARNING + \
             'Enter the query you wish to run followed by any arguments you would like to include \n' + \
             'For example: c Foster_NB 2011-09-22\n' + bcolors.ENDC
    userInput = ''
    while (True):
        userInput = raw_input(prompt)
        if userInput.upper() == 'EXIT' or userInput.upper() == 'Q':
            break
        elif userInput.upper() == 'HELP':
            help()
        else:
            args = userInput.split(' ')[1:]
            query = userInput.split(' ')[0]
            call_query(conn, query.upper(), args)
        raw_input('Press enter to continue...')
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
