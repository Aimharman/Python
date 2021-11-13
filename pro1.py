import sys
import csv

delimit = ','
infile = open('C:\\Users\\ankes\\Documents\\Python Scripts\\data.csv', 'r')
newdata = []
storedata = []
rows = 0
for row in csv.reader(infile,delimiter=delimit):
    rows += 1
    if rows < 102:
        newdata.append(row)
storedata = newdata
print("Writing to Sourcelocal.csv....")
rows = -1
with open('Sourcelocal.csv','w',newline = '') as newfile:
    writer = csv.writer(newfile)
    for row in storedata:
        rows += 1
        if rows < 101:
            writer.writerow(storedata[rows])
print("Total No. of rows updated: ", rows)

rows = 0    
colcount = 0
for row in newdata:
    rows += 1
    if colcount < 1:
        try:
            data = newdata[0][rows]
        except IndexError as error:
            print("Last Column Reached!!")
            cols = rows
            colcount = 1
                
            
print("Last Row Reached!!")
print("No. of columns in CSV: ", cols)
print("No. of rows in CSV: ", rows)

print("Writing to newfile.csv....")
rows = 0    
with open('newfile.csv','w',newline = '') as modfile:
    moder = csv.writer(modfile)
    div = 1000000
    data1 = 0
    data2 = 0
    for row in newdata:
        if rows == 0:
            row.append("Profit ($ million)")
            newdata[rows][2] = "Budget ($ million)"
            newdata[rows][3] = "Gross ($ million)"
        else:
            data1 = int(newdata[rows][2]) // div
            newdata[rows][2] = str(data1)
            data2 = int(newdata[rows][3]) // div
            newdata[rows][3] = str(data2)
            row.append(data2 - data1)
        moder.writerow(row)
        rows += 1
    print("Total No. of rows updated: ", rows) 

# Sorting Data -------- Bubble Sorting
print("Sorting Dataframe as per Profit Column in descending order")
# First covert str dataframe to int :
rows = 0
cols = 0
sort = []
for row in newdata:
    if rows < 100:    
        rows += 1
        sort.append(int(newdata[rows][62]))

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

# Output sorted dataframe to CSV

# First arrange the Dataframe

sortsource = []
sortsource = newdata
sortedframe = []
sortedframe.append(sortsource[0])
ite = 0
while ite < 100:
    rows = -1
    for row in sortsource:
        rows += 1
        if rows > 0:
            temp = int(sortsource[rows][62])
            if temp == sort[ite]:
                sortedframe.append(row)
                del sortsource[rows]
    ite += 1

#Write the sorted Dataframe to CSV.
print("Writing to newfile.csv....")
rows = -1
with open('newfile.csv','w',newline = '') as sortframefile:
    writer = csv.writer(sortframefile)
    for row in sortedframe:
        rows += 1
        if rows < 101:
            writer.writerow(sortedframe[rows])
print("Total No. of rows updated: ", rows+1)

infile.close