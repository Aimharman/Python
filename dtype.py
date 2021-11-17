list1 = []
temp = [0, 0, 0, 0, 0]
list1.append(temp)
list1.append(temp)
list1.append(temp)
list1[0] = 2016, 7, 15, 19, 40
list1[1] = 2016, 8, 17, 22, 23
list1[2] = 2016, 5, 14, 21, 54

print(list1)

temp = list1[0]
list1[0] = list1[1]
list1[1] = temp
temp1=[]
temp1 = list1[0]

print(temp1)
