# Optimised bubble sort for sortin values

list = [24,24,24,24,245,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24]
list1 = [27,84,64,24,245,249,424,124,94,56,47,67,32,31,765,453,398,825,77,73,14,39,43,34]

print ("List: ",list)
print ("List1: ",list1)

item = 1
for i in list:
    try:
        temp = list[item]
    except IndexError as error:
        print ("Length of List: ", item)
    item += 1

item = 1
for i in list1:
    try:
        temp = list1[item]
    except IndexError as error:
        print ("Length of List1: ", item)
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

print ("Sorted List: ",list)
print ("Iterator run: ",count, "times")

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
            temp = list1[item+1]
        except IndexError as error:
            item = 0 
            print("Error")
    while ite < 23:
        if list1[ite] < list1[ite+1]:
            incount = 1
            temp = list1[ite]
            list1[ite] = list1[ite+1]
            list1[ite+1] = temp
        ite += 1
    item = 0
    iterate = 1

print ("Sorted List1: ", list1)
print ("Iterator run: ",count, "times")
