# Some data manipulation techniques without numpy and pandas!! ---> Important concepts.

import sys
#import matplotlib.pyplot as plt

# Reading Data from a CSV file ---------- Without Pandas & Numpy

delimit = ','
infile = open('C:/Users/ankes/Desktop/data_stored.csv', 'r')
import csv
newdata = []
rows = 0
for row in csv.reader(infile,delimiter=delimit):
    rows += 1
    if rows >= 0:
        newdata.append(row)
    
rows = -1

# To find total list items in vector infile

infile.seek(0)
ncol = len(next(infile))
print("Total number of data items in list vector: ",ncol)
print(newdata[5][0])

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

row_iterator = rows
col_iterator = cols                 
print("Last Row Reached!!")
print("No. of columns in CSV: ", cols)
print("No. of rows in CSV: ", rows)
#print(newdata)

# First covert str dataframe to int :
rows = 0
sort = []
for row in newdata:
    if rows < row_iterator - 1 : 
        try:   
            rows += 1
            #print(int ((newdata[rows][0])))
            sort.append(int(newdata[rows][0]))
        except ValueError:
            break


rpeak_index = []
rpeak = []
identifier_matrix = []
rows = 0
cnt_c = 0
temp = 0
for row in sort:
    if rows < row_iterator - 1 : 
        try:   
            rows += 1
            if((((sort[rows]) > 391000))):
                #print(sort[rows])
                rpeak_index.append(rows)
                rpeak.append(sort[rows])
                var = rows - temp
                identifier_matrix.insert(cnt_c,[sort[rows], rows, var])
                cnt_c += 1
                temp = rows
        except ValueError:
            break
        except IndexError:
            break
#print(rpeak_index)
#print(rpeak)
print("Identifier Matrix>>>\n",identifier_matrix)

sample_diff = []
rows = 0
for row in rpeak_index:
    if rows < row_iterator - 1 :
        try:   
            rows += 1
            var = rpeak_index[rows] - rpeak_index[rows-1]
            sample_diff.append(var)
        except ValueError:
            break
        except IndexError:
            break
#print(sample_diff)
sample_count = rows

reference = []
rows = 0
for row in sample_diff:
    if rows <= sample_count : 
        try:   
            #print(int ((newdata[rows][0])))
            reference.append(sample_diff[rows])
            rows += 1
        except ValueError:
            break
        except IndexError:
            break


rows = 0
rows2 = 0
unique_value_count = []
cnt_c = 0
#print(sample_diff)
#print(reference)

repeat_count = 0
for row in reference:
    if rows < 2*sample_count :
        try:
            if(reference[rows] == 0):
                rows+=1
                rows2 += 1
            if(rows!=0):
                rows2 = rows
            var = reference[rows]
            repeat_count = 1
            #print(var)
            for row in reference:
                try:
                    if(var == 0):
                        break
                    rows2 += 1
                    #print(var, reference[rows2])
                    if(var == reference[rows2]):
                        reference[rows2] = 0
                        repeat_count += 1    
                except ValueError:
                    print("value_inner")
                    break
                except IndexError:
                    #print(var, "-", repeat_count)
                    unique_value_count.insert(cnt_c,[var,repeat_count])
                    rows += 1
                    cnt_c += 1
                    #print("index_inner")
                    break
        except ValueError:
            print("value_outer")
            break
        except IndexError:
            print("\nIterations Completed!\n")
            break
#print(reference)
print("R Peak Periodicity in Samples>>>>>>   ", unique_value_count)
