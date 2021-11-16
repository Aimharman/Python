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

#def ord_date_time(tripcomp)

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
#print (ordlist)

# Preparing single dimension list of each date-time attribute for sorting & plotting

Ylist = []
rows = 0
for row in ordlist:
    tempest = [0]
    Ylist.append(tempest)
    Ylist[rows][0] = ordlist[rows][0] 
    rows += 1
#print (Ylist)

Mlist = []
rows = 0
for row in ordlist:
    tempest = [0]
    Mlist.append(tempest)
    Mlist[rows][0] = ordlist[rows][1] 
    rows += 1
#print (Mlist)

Dlist = []
rows = 0
for row in ordlist:
    tempest = [0]
    Dlist.append(tempest)
    Dlist[rows][0] = ordlist[rows][2] 
    rows += 1
#print (Dlist)

Hlist = []
rows = 0
for row in ordlist:
    tempest = [0]
    Hlist.append(tempest)
    Hlist[rows][0] = ordlist[rows][3] 
    rows += 1
#print (Hlist)

mlist = []
rows = 0
for row in ordlist:
    tempest = [0]
    mlist.append(tempest)
    mlist[rows][0] = ordlist[rows][4] 
    rows += 1
#print (mlist)


sort = mlist
# Optimized bubble sort algorithm for implementation

item = 1
for i in sort:
    try:
        temp = sort[item]
    except IndexError as error:
        print ("Length of List: ", item)
    item += 1
lenoflist = item - 2

item = 0
ite = 0
iterate = 0
incount = 1
count = 0
while incount > 0:
    count += 1
    ite = 0
    incount = 0
    if iterate > 0:
        try:
            temp = sort[item+1]
        except IndexError as error:
            item = 0 
            print("Error")
    while ite < lenoflist:
        if sort[ite] < sort[ite+1]:
            incount = 1
            temp = sort[ite]
            sort[ite] = sort[ite+1]
            sort[ite+1] = temp
        ite += 1
    item = 0
    iterate = 1

#print ("Sorted List: ",sort)
print ("Iterator run: ",count, "times")

infile.close