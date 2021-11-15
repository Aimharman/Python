import csv
import os
import errno

Data_Frame = []
infile = open('C:\\Users\\ankes\\Documents\\Python Scripts\\uber.csv', 'r')
rows = 0
colendcount = 0
for row in csv.reader(infile, delimiter = ','):
    try:
        xyz = row[rows]
    except IndexError:
        if colendcount < 1:
            print("Number of columns in Data Frame: ", rows)
            colendcount += 1
    rows += 1
    Data_Frame.append(row)
print("Number of rows in Data Frame: ",rows)

#for row in Data_Frame:
#    print (row,"\n")
#print(Data_Frame)

# Segregating Data Frames based on trip completion.

tripcomplete = []
tripdroped = []
carshortage = []
rows = 0
for row in Data_Frame:
    if Data_Frame[rows][3] == 'Trip Completed':
        tripcomplete.append(row)
    elif Data_Frame[rows][3] == 'Cancelled':
        tripdroped.append(row)
    else:
        carshortage.append(row)
    rows += 1

# Created new folder for keeping intermediate data frames

try:
    os.mkdir('C:\\Users\\ankes\\Documents\\Python Scripts\\uber\\')
except OSError:
    print("uber folder exists in directory!")

# Writing data frames to csv

outfile = open('C:\\Users\\ankes\\Documents\\Python Scripts\\uber\\tripcompleted.csv', 'w', newline ='')
writer = csv.writer(outfile)
for row in tripcomplete:
    writer.writerow(row)
outfile.close

outfile = open('C:\\Users\\ankes\\Documents\\Python Scripts\\uber\\tripdropped.csv', 'w', newline ='')
writer = csv.writer(outfile)
for row in tripdroped:
    writer.writerow(row)
outfile.close

outfile = open('C:\\Users\\ankes\\Documents\\Python Scripts\\uber\\carshortage.csv', 'w', newline ='')
writer = csv.writer(outfile)
for row in carshortage:
    writer.writerow(row)
outfile.close

#print (tripcomplete)

# Extracting columns needed for plot in single dimension list[]

