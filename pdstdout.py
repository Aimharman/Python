import pandas as pd
#import csv
data = pd.read_csv('C:\\Users\\ankes\\Documents\\Python Scripts\\data.csv')
print(data)
halt = int(input())
if(halt>10):
	print(data[0:5]['Title'])
else:
	print(data.loc[0:5,['Title','VotesUS']])
	
halt = int(input())
if(halt==1):
	print(data.loc[:,['Title','VotesUS']])
else:
	print(data[0:5])
    
#with open('C:\\Users\\ankes\\Documents\\Python Scripts\\data.csv', 'r') as file:
#    reader = csv.reader(file)
#   count = 0
#    newdata = []
#    print("Hello")
#    for row in data:
#        newdata.append(row[count])
#        count+=1
#        print(newdata)

infile = open('C:\\Users\\ankes\\Documents\\Python Scripts\\data.csv', 'r')
import csv
newdata = []
rows = 0
for row in csv.reader(infile):
    rows += 1
    if rows < 102:
        newdata.append(row)
    infile.close
    
print(newdata)
print(newdata[10])

   
with open('newfile.csv','w') as newfile:
    writer = csv.writer(newfile)
    writer.writerow(newdata)	