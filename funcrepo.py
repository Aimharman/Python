#-----------------------------------------------1----------------------------------------------------

# Optimized bubble sort algorithm for implementation

def sortlist(sorty):
    item = 1
    sort = sorty
    for i in sort:
        try:
            temp = sort[item]
        except IndexError as error:
            print ("Length of List: ", item)
        item += 1
    lenoflist = item - 2

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
                temp = sort[item+1]
            except IndexError as error:
                item = 0 
                print("Error")
        while ite < lenoflist:
            if sort[ite] < sort[ite+1]:
                incount = 1
                temp = sort[ite]
                sort[ite] = sort[ite+1]
                sort[ite+1] = temp
            ite += 1
        item = 0
        iterate = 1

    #print ("Sorted List: ",sort)
    #print ("Iterator run: ",count, "times")
    #print ("Note:- If interator run is single then there is nothing to sort, all rows have same value!\n\n")
    return sort


#-----------------------------------------------2----------------------------------------------------


# First arrange the Dataframe
def arrangeDF(sort_source, compare, rowcnt, colcount):
    #rows = -1
    sortsource = sort_source
    sort = compare
    sortedframe = []
    ite = 0
    while ite < rowcnt:
        rows = -1
        for row in sortsource:
            rows += 1
            if rows > 0:
                temp = []
                temp.append(sortsource[rows][colcount])
                try:
                    if temp == sort[ite]:
                        #print (row)
                        sortedframe.append(row)
                        del sortsource[rows]
                except IndexError:
                    break
        #print ("Ïtem No:", ite)
        ite += 1
    #print (sortedframe)
    return sortedframe


#-----------------------------------------------3----------------------------------------------------

# Transforming time stamp entries to usable format.

from datetime import datetime
ordlist = []
rows = 0
cnt = 0
for row in tripcomplete:
    if rows > 0:
        var = (datetime.strptime(tripcomplete[rows][4], "%d/%m/%Y %H:%M"))
        tempest = [0,1,2,3,4]
        ordlist.append(tempest)
        ordlist[cnt][0] = var.year
        ordlist[cnt][1] = var.month
        ordlist[cnt][2] = var.day
        ordlist[cnt][3] = var.hour
        ordlist[cnt][4] = var.minute
        #print(var)
        cnt += 1
    rows += 1
print (ordlist)


#-----------------------------------------------4----------------------------------------------------

# Preparing single dimension list of each date-time attribute for sorting & plotting

Ylist = []
rows = 0
for row in ordlist:
    tempest = [0]
    Ylist.append(tempest)
    Ylist[rows][0] = ordlist[rows][0] 
    rows += 1
#print (Ylist)


#-----------------------------------------------5----------------------------------------------------

# Successive sorting algorithm

if foh == 0:
    print(fod, "Hello")
    if fod == 2:
        print(fod, "hello")
        rows = 0
        rows1 = 1
        countiter = 0
        flag = 0
        rowprev = 0
        delta = 0
        dribblelist = []
        #dribblelist = Data_Frame_date
        for row in Data_Frame_date:
            try:
                Data_Frame_date[rows1]
            except IndexError:
                print("ëxception")
            
            if rows == 2829:
                flag = 1
               
            if rows < 2829:    
                if Data_Frame_date[rows][2] == Data_Frame_date[rows1][2] and rows < 2828:
                    dribblelist.append(row)
                    delta += 1
                    rows += 1
                    rows1 += 1
                    #countiter += 1
                    #print("rows: ", rows)
                else:
                    dribblelist.append(row)
                    i = 1
                    temp = []
                    if countiter < 1:
                        rowcntrec = 0
                        rowcntrec1 = 1
                    elif countiter > 0:
                        rowcntrec = rows - delta - countiter
                        rowcntrec1 = rowcntrec + 1
                    delta = 0
                    iterstop = 3
                    rowprev = rows
                    while i:
                        j = rowcntrec
                        if iterstop < 3:
                            break
                        rown = rowcntrec
                        rown1 = rowcntrec1
                        print("rown:", rown, "rows:", rows)
                        #print(dribblelist)
                        iterstop = 2
                        range = rows
                        while j<range:
                            #print("j: ", j)
                            comp = dribblelist[rown][3]
                            comp1 = dribblelist[rown1][3]
                            
                            if comp > comp1:
                                temp = dribblelist[rown]
                                dribblelist[rown] = dribblelist[rown+1]
                                dribblelist[rown+1] = temp
                                iterstop += 1
                            rown += 1
                            rown1 += 1
                            j+=1
                        i += 1
                    rows += 1
                    rows1 += 1
                    countiter += 1
                    print("countiter: ", countiter)
                if flag == 1:
                    break
                
print(dribblelist, "\n\nNumber of rows:", rows, "\nIterations: ", i)    
#print("\n\n\n\n", Data_Frame_date)

#-----------------------------------------------6----------------------------------------------------

# Lowest Selection Sort

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

#-----------------------------------------------7----------------------------------------------------

# Merge Sort

#dribble_list = [80,70,60,40,33,22,5,9]
unsorted_list = Data_Frame1
#print(dribble_list)

rangel = len(unsorted_list)
print(rangel)



def merge_sort(unsorted_list):
   if len(unsorted_list) <= 1:
      return unsorted_list
# Find the middle point and devide it
   middle = len(unsorted_list) // 2
   left_list = unsorted_list[:middle]
   right_list = unsorted_list[middle:]

   left_list = merge_sort(left_list)
   right_list = merge_sort(right_list)
   return list(merge(left_list, right_list))

# Merge the sorted halves
def merge(left_half,right_half):
   res = []
   while len(left_half) != 0 and len(right_half) != 0:
      if left_half[0] < right_half[0]:
         res.append(left_half[0])
         left_half.remove(left_half[0])
      else:
         res.append(right_half[0])
         right_half.remove(right_half[0])
   if len(left_half) == 0:
      res = res + right_half
   else:
      res = res + left_half
   return res
#unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print(merge_sort(unsorted_list))

