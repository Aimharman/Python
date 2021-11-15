import csv
infile = open('C:\\Users\\ankes\\Documents\\Python Scripts\\uber\\tripcompleted.csv', 'r')
rows = 0
colendcount = 0
tripcomplete = []
for row in csv.reader(infile, delimiter = ','):
    try:
        xyz = row[rows]
    except IndexError:
        if colendcount < 1:
            print("Number of columns in Data Frame: ", rows)
            colendcount += 1
    rows += 1
    tripcomplete.append(row)
print("Number of rows in Data Frame: ",rows)

# Metod to extract date-time format data stored in str format when imported into list from CSV

from datetime import datetime
ordlist = []
rows = 0
cnt = 0
for row in tripcomplete:
    if rows > 0:
        var = (datetime.strptime(tripcomplete[rows][4], "%d/%m/%Y %H:%M"))
        tempest = [0,1,2,3,4]
        ordlist.append(tempest)
        ordlist[cnt][0] = var.year
        ordlist[cnt][1] = var.month
        ordlist[cnt][2] = var.day
        ordlist[cnt][3] = var.hour
        ordlist[cnt][4] = var.minute
        #print(var)
        cnt += 1
    rows += 1
print (ordlist)


infile.close