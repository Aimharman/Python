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

rows = -1
with open('Sourcelocal.csv','w',newline = '') as newfile:
    writer = csv.writer(newfile)
    for row in storedata:
        rows += 1
        if rows < 101:
            writer.writerow(storedata[rows])

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

rows = 0    
with open('newfile.csv','w',newline = '') as modfile:
    moder = csv.writer(modfile)
    #print (int(newdata[1][2]))
    div = 1000000
    data = 0
    for row in newdata:
        if rows == 0:
            newdata[rows][2] = "Budget ($ million)"
            newdata[rows][3] = "Gross ($ million)"
        else:
            data = int(newdata[rows][2]) // div
            newdata[rows][2] = str(data)
            data = int(newdata[rows][3]) // div
            newdata[rows][3] = str(data)
        moder.writerow(row)
        rows += 1
    print("Total No. of rows updated: ", rows) 

infile.close