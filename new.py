import csv
with open('data.csv','r') as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    fields = next(reader)
    for row in reader:
        row.append(row)
        print("Total no. of rows: %d"%(reader.line_num))   
        
    print (fields)