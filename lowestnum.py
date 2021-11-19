lista = [80,70,60,40,33,22,5,9]
rangel = len(lista)
dribble_list = lista
a = 0
maximum = 0
while(a<rangel):
    maximum = maximum > dribble_list[a] and maximum or dribble_list[a]
    a += 1 
#print("max: ", maximum)
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
            temp = 100
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

