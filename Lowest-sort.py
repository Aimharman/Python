dribble_list = [80,70,60,40,33,22,5,9]
rangel = len(dribble_list)
a = 0 
maximum = 0
while(a<rangel):
    maximum = maximum > dribble_list[a] and maximum or dribble_list[a]
    a += 1 
temp = maximum + 1
a = 0
count = 0
rows = 0
while a < rangel:
    for i in dribble_list:
        try:
            n = dribble_list[rows + 1]
        except IndexError:
            count += 1
            rows = count
            b = count-1
            while (b < (rangel-1)):
                b+=1
                if dribble_list[b] == temp:
                    temp_int = dribble_list[count-1]
                    dribble_list[count-1] = temp
                    dribble_list[b] = temp_int
            if (count > (rangel-2)):
                count = 0    
            temp = maximum + 1
        else:
            if dribble_list[rows] < dribble_list[rows+1]:
                temp = temp < dribble_list[rows] and temp or dribble_list[rows]
                rows += 1
            else:
                temp = temp < dribble_list[rows+1] and temp or dribble_list[rows+1]
                rows += 1
    a+=1
print("Lowest Number: ",dribble_list[0])
print(dribble_list)

