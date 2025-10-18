# There are two algorithms here, but only one is implemented
# The first one , i gave it the name "minSort", is based, on
# 1) Get minimum of list, and put it in first on other list
# 2) Get differences (we can consider differences as "distance" between numbers)
# and put them in a list
#
# For example, we have a list of numbers
# [4,2,7,1] ...first element 1 ,so rearranje list, this gives us
# [1,4,2,7] minimum number ordered.
#Calculate distances of numbers, from one (zero index), to other positions
# Distances = [0,3,1,6] ..e.g on second index, 4 is at a distance of 3 from first elem (zero)
# So use that

# 2 algorihm
# TRaverse the list, get minimum, remove element from list, get minimum again
# Can be use on ascending or descending order, and handles repetitions, as well..

def minSort(l):
    sortedList = []
    for it in range(0,len(l)):
        minAux = min(l)
        sortedList.append(minAux)
        l.remove(minAux)
    return sortedList

#Example
#test  = minSort([4,2,1,5,32,2,2,43,0,23,2,7,3,2,1,2,4,7])
#print(test)

