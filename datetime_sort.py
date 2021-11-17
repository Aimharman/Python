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
print("Number of rows in Data Frame: ",rows,"\n\n")
rowcount = rows

# Optimized bubble sort algorithm for implementation

def sortlist(sorty):
    item = 1
    sort = sorty
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
    #print ("Iterator run: ",count, "times")
    #print ("Note:- If interator run is single then there is nothing to sort, all rows have same value!\n\n")
    return sort

def count(sorty):
    item = 1
    sort = sorty
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
    print ("Note:- If interator run is single then there is nothing to sort, all rows have same value!\n\n")
    return count


# First arrange the Dataframe
def arrangeDF(sort_source, compare, rowcnt, colcount):
    #rows = -1
    sortsource = sort_source
    sort = compare
    sortedframe = []
    ite = 0
    while ite < rowcnt:
        rows = -1
        for row in sortsource:
            rows += 1
            if rows > 0:
                temp = []
                temp.append(sortsource[rows][colcount])
                #sort[ite] = int(sort[ite])
                #print (temp, "&", sort[ite])
                #print(sortsource[rows][0])
                try:
                    if temp == sort[ite]:
                        #print (row)
                        sortedframe.append(row)
                        del sortsource[rows]
                except IndexError:
                    break
        #print ("Ïtem No:", ite)
        ite += 1
    #print (sortedframe)
    return sortedframe


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
templist = []
templist = ordlist

# Preparing single dimension list of each date-time attribute for sorting & plotting

Ylist = []
rows = 0
for row in ordlist:
    tempest = [0]
    Ylist.append(tempest)
    Ylist[rows][0] = ordlist[rows][0] 
    rows += 1
#print (Ylist)
iteratorY = count(Ylist)
Ylist = sortlist(Ylist)

Mlist = []
rows = 0
for row in ordlist:
    tempest = [0]
    Mlist.append(tempest)
    Mlist[rows][0] = ordlist[rows][1] 
    rows += 1
#print (Mlist)
iteratorM = count(Mlist)
Mlist = sortlist(Mlist)

Dlist = []
rows = 0
for row in ordlist:
    tempest = [0]
    Dlist.append(tempest)
    Dlist[rows][0] = ordlist[rows][2] 
    rows += 1
#print (Dlist)
iteratorD = count(Dlist)
Dlist = sortlist(Dlist)
#print (Dlist)

Hlist = []
rows = 0
for row in ordlist:
    tempest = [0]
    Hlist.append(tempest)
    Hlist[rows][0] = ordlist[rows][3] 
    rows += 1
#print (Hlist)
iteratorH = count(Hlist)

mlist = []
rows = 0
for row in ordlist:
    tempest = [0]
    mlist.append(tempest)
    mlist[rows][0] = ordlist[rows][4] 
    rows += 1
#print (mlist)
iteratorm = count(mlist)

# Flags:

foy = 0
fom = 0
fod = 0
foh = 0
formi = 0

iter = 5
while iter > 0:
    if iteratorY == 1 and iter == 5:
        print("Year Col: All data belongs to same year!")
        foy = 1
        iter += -1
        continue
    elif iteratorM == 1 and iter == 4:
        print("Month Col: All data belongs to same month!")
        fom = 1
        iter += -1
        continue
    elif iteratorD == 1 and iter == 3:
        print("Day Col: All data belongs to same day!")
        fod = 1
        iter += -1
        continue
    elif iteratorH == 1 and iter == 2:
        print("Hour Col: All data belongs to same hour!")
        foh = 1
        iter += -1
        continue
    elif iteratorm == 1 and iter == 1:
        print("Minutes Col: All data belongs to same minutes!")
        fomin = 1
        iter += -1
        break
    break

# Sorting Data Frame
# First Sort Check Year
print("foy, fom, fod, foh, formi :",foy, fom, fod, foh, formi)
Data_Frame_date = []

if foy == 0:
    Data_Frame_date = arrangeDF(templist, Ylist, rowcount, 0)
    foy = 2
#Data_Frame_date = arrangeDF(templist, Ylist, rowcount, 0)

if fom == 0:
    if foy == 1:
        Data_Frame_date = arrangeDF(templist, Mlist, rowcount, 1)
        fom = 2

if fod == 0:
    if fom == 1:
        #print("Hello")
        Data_Frame_date = arrangeDF(templist, Dlist, rowcount, 2)
        fod = 2

intsortlist = []
if foh == 0:
    print(fod, "Hello")
    if fod == 2:
        print(fod, "hello")
        rows = 0
        rows1 = 1
        countiter = 0
        flag = 0
        rowprev = 0
        delta = 0
        dribblelist = []
        #dribblelist = Data_Frame_date
        for row in Data_Frame_date:
            try:
                Data_Frame_date[rows1]
            except IndexError:
                print("ëxception")
            
            if rows == 2829:
                flag = 1
               
            if rows < 2829:    
                if Data_Frame_date[rows][2] == Data_Frame_date[rows1][2] and rows < 2828:
                    dribblelist.append(row)
                    delta += 1
                    rows += 1
                    rows1 += 1
                    #countiter += 1
                    #print("rows: ", rows)
                else:
                    dribblelist.append(row)
                    i = 1
                    temp = []
                    if countiter < 1:
                        rowcntrec = 0
                        rowcntrec1 = 1
                    elif countiter > 0:
                        rowcntrec = rows - delta - countiter
                        rowcntrec1 = rowcntrec + 1
                    delta = 0
                    iterstop = 3
                    rowprev = rows
                    while i:
                        j = rowcntrec
                        if iterstop < 3:
                            break
                        rown = rowcntrec
                        rown1 = rowcntrec1
                        print("rown:", rown, "rows:", rows)
                        #print(dribblelist)
                        iterstop = 2
                        range = rows - countiter - 1
                        while j<range:
                            print("j: ", j)
                            comp = dribblelist[rown][3]
                            comp1 = dribblelist[rown1][3]
                            
                            if comp > comp1:
                                temp = dribblelist[rown]
                                dribblelist[rown] = dribblelist[rown+1]
                                dribblelist[rown+1] = temp
                                iterstop += 1
                            rown += 1
                            rown1 += 1
                            j+=1
                        i += 1
                    rows += 1
                    rows1 += 1
                    countiter += 1
                    print("countiter: ", countiter)
                if flag == 1:
                    break
                
print(dribblelist, "\n\nNumber of rows:", rows, "\nIterations: ", i)    
#print("\n\n\n\n", Data_Frame_date)
outfile = open('C:\\Users\\ankes\\Documents\\Python Scripts\\uber\\uberdribble.csv', 'w', newline ='')
writer = csv.writer(outfile)
for row in dribblelist:
    writer.writerow(row)
outfile.close

outfile = open('C:\\Users\\ankes\\Documents\\Python Scripts\\uber\\uberdribble1.csv', 'w', newline ='')
writer = csv.writer(outfile)
for row in Data_Frame_date:
    writer.writerow(row)
outfile.close