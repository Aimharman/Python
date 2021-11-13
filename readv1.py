import sys

# Reading Data from a CSV file ---------- Without Pandas & Numpy
sortsource = []
delimit = ','
infile = open('C:\\Users\\ankes\\Documents\\Python Scripts\\newfile.csv', 'r')
import csv
newdata = []
rows = 0
for row in csv.reader(infile,delimiter=delimit):
    rows += 1
    if rows < 102:
        newdata.append(row)
        #print(newdata)
#infile.close
#sortsource = newdata
rows = -1

# To find total list items in vector infile

infile.seek(0)
ncol = len(next(infile))
print("Total number of data items in list vector: ",ncol)
#print(newdata)
print(newdata[4][5])

# Copying Data from source CSV file to new CSV file

rows = -1
with open('dribble.csv','w',newline = '') as newfile:
    writer = csv.writer(newfile)
    for row in newdata:
        rows += 1
        if rows < 101:
            writer.writerow(newdata[rows])

# Modify: Adding column or data to any row in data frame ----- Without Pandas & Numpy

rows = 0    
with open('dribble.csv','w',newline = '') as modfile:
    moder = csv.writer(modfile)
    for row in newdata:
        if rows == 0:
            row.append("Name")
            rows += 1
        moder.writerow(row)
        #if rows == 1:
        #    break
            
           
# Counting Rows & Columns in CSV --------------------------- Without Pandas & Numpy

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

# Sorting Data -------- Bubble Sorting

# First covert str dataframe to int :
rows = 0
cols = 0
sort = []
ordsort = []
for row in newdata:
    if rows < 100:    
        rows += 1
        #print (newdata[rows][62])
        sort.append(int(newdata[rows][62]))

print(sort)


# Then implement sorting algorithm :

item = 0   
iter = 0
iterate = 1
counter = 0
#print (sort[item+1], sort[item])s
while iter < 4000 :
    #print("MC")
    if iterate > 0:
        try:
            trye = sort[item+1]
        except IndexError as error:
            item = 0
            counter += 1
    if sort[item] < sort[item+1] :
        iterate = 1
        temp = sort[item]
        sort[item] = sort[item + 1]
        sort[item + 1] = temp
        #print(sort[item])
    item += 1
    iter += 1    

print("\n\n",sort)

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

print ("Sorted List: ",sort)
print ("Iterator run: ",count, "times")

# Output sorted dataframe to CSV

# First arrange the Dataframe
#rows = -1
sortsource = newdata
sortedframe = []
ite = 0
while ite < 100:
    rows = -1
    for row in sortsource:
        rows += 1
        if rows > 0:
            temp = int(sortsource[rows][62])
            #print (temp, "&", sort[ite])
            if temp == sort[ite]:
                #print (row)
                sortedframe.append(row)
                del sortsource[rows]
    #print ("Ïtem No:", ite)
    ite += 1
#print (sortedframe)

#Write the sorted Dataframe to CSV.

rows = -1
with open('dribble.csv','w',newline = '') as sortframefile:
    writer = csv.writer(sortframefile)
    for row in sortedframe:
        rows += 1
        if rows < 101:
            writer.writerow(sortedframe[rows])
infile.close
