
list = [24,24,24,24,245,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24]
print (list)

item = 1
for i in list:
    try:
        temp = list[item]
    except IndexError as error:
        print "Length of List: ", item
    item += 1
    

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
            temp = list[item+1]
        except IndexError as error:
            item = 0 
            print("Error")
    while ite < 23:
        if list[ite] < list[ite+1]:
            incount = 1
            temp = list[ite]
            list[ite] = list[ite+1]
            list[ite+1] = temp
        ite += 1
    item = 0
    iterate = 1

print (list)
print "Count Value: ",count
        
        
