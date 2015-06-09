import csv

f = open('/u/giossic/Downloads/ProjectDataCloud2015/ProjectData-Cloud2015/highways.csv', 'rU')
highways = csv.reader(f)
highways = list(highways)
f.close()
f = open('/u/giossic/Downloads/ProjectDataCloud2015/ProjectData-Cloud2015/freeway_detectors.csv', 'rU')
detectors = csv.reader(f)
detectors = list(detectors)
f.close()
f = open('/u/giossic/Downloads/ProjectDataCloud2015/ProjectData-Cloud2015/freeway_stations.csv', 'rU')
stations = csv.reader(f)
stations = list(stations)
f.close()
f = open('/u/giossic/Downloads/ProjectDataCloud2015/ProjectData-Cloud2015/freeway_loopdata.csv', 'rU')
loopdata = csv.reader(f)
headers = loopdata.next()

new_headers = headers + [stations[0][4]] + [stations[0][5]] + [stations[0][7]] + \
              [stations[0][8]] + [stations[0][9]] + [stations[0][3]] + \
              [detectors[0][6]] + [detectors[0][2]] + [detectors[0][4]] + \
              [detectors[0][5]] + [highways[0][0]] + [highways[0][2]] + \
              [highways[0][3]]

csvfilenames = {}

for row in stations[1:]:
    csvfilenames[row[3]] = csv.writer(open('/u/giossic/joined/' + row[3].replace('/', '-') + '.csv', 'wb'))

for key in csvfilenames.keys():
    csvfilenames[key].writerow(new_headers)

newRow = []
for row in loopdata:
    newRow = row
    curId = row[0]
    curSID = 0
    curHID = 0
    for i in detectors:
        if curId == i[0]:
            curSID = i[6]
            curHID = i[1]
    if curSID == 0:
        continue
    for i in stations:
        if curSID == i[0]:
            newRow += [i[4]]
            newRow += [i[5]]
            newRow += [i[7]]
            newRow += [i[8]]
            newRow += [i[9]]
            newRow += [i[3]]
    for i in detectors:
        if curId == i[0]:
            newRow += [i[6]]
            newRow += [i[2]]
            newRow += [i[4]]
            newRow += [i[5]]
    for i in highways:
        if curHID == i[0]:
            newRow += [i[0]]
            newRow += [i[2]]
            newRow += [i[3]]
    csvfilenames[newRow[12]].writerow(newRow)

f.close()
