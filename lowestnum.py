import csv
Data_Frame = []
Data_Frame1 = []
infile = open('C:\\Users\\ankes\\Documents\\Python Scripts\\inp.csv', 'r')
rows = 0
colendcount = 0
var = 0
for row in csv.reader(infile, delimiter = ','):
    try:
        xyz = row[rows]
    except IndexError:
        if colendcount < 1:
            print("Number of columns in Data Frame: ", rows)
            colendcount += 1
    rows += 1
    Data_Frame.append(row)
    var = int(float(Data_Frame[rows-1][0]))
    Data_Frame1.append(var)
    
    
print("Number of rows in Data Frame: ",rows)
#var = Data_Frame[1][0]
#print(var, type(var))    

#dribble_list = [80,70,60,40,33,22,5,9]
dribble_list = Data_Frame1
#print(dribble_list)
rangel = len(dribble_list)
#print(rangel)

a = 0
maximum = 0
while(a<rangel):
    maximum = maximum > dribble_list[a] and maximum or dribble_list[a]
    a += 1 
print("max: ", maximum)
temp = maximum
a = 0
count = 0
rows = 0
while a < rangel:
    for i in dribble_list:
        # This is three step iterator in series starting from try & ending @ else so place incrementer carefully!
        try:
            n = dribble_list[rows + 1]
        except IndexError:
            count += 1
            rows = count
            b = count-1
            while (b < (rangel-1)):
                b+=1
                #print("dribble_list[0], temp: ", dribble_list[b], temp)
                if dribble_list[b] == temp:
                    temp_int = dribble_list[count-1]
                    dribble_list[count-1] = temp
                    dribble_list[b] = temp_int
                    #print("dribble_list[count-1], dribble_list[b]: ",dribble_list[count-1], dribble_list[b])
            if (count > (rangel-2)):
                count = 0    
            temp = maximum + 100
        else:
            #print ("rows, ", rows)
            #print("dribble_list[rows], dribble_list[rows+1]: ",dribble_list[rows], dribble_list[rows+1])
            if dribble_list[rows] < dribble_list[rows+1]:
                temp = temp < dribble_list[rows] and temp or dribble_list[rows]
                rows += 1
            else:
                temp = temp < dribble_list[rows+1] and temp or dribble_list[rows+1]
                rows += 1
        #print("temp: ",temp)
        
    a+=1
print("Lowest Number: ",dribble_list[0])
print(dribble_list)

