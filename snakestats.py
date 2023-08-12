
# TEST SET 1:
"""
===========================================
Test set 1 test 1(updated to mode function)
===========================================
"""
def find_count(mylist):
    counts=[]
    for i in range(len(mylist)):

            #count number 1 and 2,pass in counts
            counts += [mylist.count(mylist[i])]

            #find the maximum count 
            max_count = max(counts)

    return max_count


"""
==========================
Test set 1 test 2(updated)
==========================


def find_mode(mylist):

    #empty list to store values
    counts=[]
    for i in range(len(mylist)):

            #count number 1 and 2,pass in counts
            counts += [mylist.count(mylist[i])]

            #find the maximum count 
            max_count = max(counts)

        #get index which element has the max count
            index = counts.index(max_count)
            a=mylist[index];

    return [a]
"""


"""
============================================
Test set 1 test 3 (finalized mode function)
============================================
"""
def find_mode(mylist):
    #let convert list into sets so no duplicates
    myset = set(mylist)
    my_newlist = list(myset)
    counts = []

    for i in range(len(my_newlist)):

        counts += [mylist.count(my_newlist[i])]


    max_count = max(counts)
    index = counts.index(max_count)

    a=my_newlist[index];

    #this gets the other similar mode 
    for i in range(index+1,len(counts)):

        if(max_count == counts[i]):
            b=my_newlist[i]
            return [a]+[b]


    return [a]



# TEST SET 2:
"""
==========================
test set 2 test 1(updated)
==========================
def median(vals):
    n = len(vals)

    # check if odd
    if n % 2 != 0:
        middle = int((n-1)/2)
        return vals[middle]

==========================================
test set 2 test 2(updated for even length)
==========================================
 def median(vals):
    n = len(vals)

    # check if odd
    if n % 2 != 0:
        middle = int((n-1)/2)
        return vals[middle]

    # this is for even length we need to add the item from previous to add up to get middle 
    elif n%2 == 0:
        middle1 = int(n/2)
        middle2=int(n/2)-1

"""

"""
=============================================
test set 2 test 3 (finalized median function)
=============================================
"""
def median(vals):
        n = len(vals)

        #add this to unordered
        vals.sort()

        # check if odd
        if n % 2 != 0:
            middle = int((n-1)/2)
            return vals[middle]

        # this is for even length we need to add the item from previous to add up to get middle 
        elif n%2 == 0:
            middle1 = int(n/2)
            middle2=int(n/2)-1

            return (vals[middle1]+vals[middle2])/2



# TEST SET 3: 
"""
==========================
test set 3 test 1(updated)
==========================

def getLow(vals):

    lowSeen = vals[0]
    for i in range(0,len(vals)): 

        if vals[i]<lowSeen:
            lowSeen = vals[i]

    return lowSeen  

==========================
test set 3 test 2(updated)
==========================

def getLow(vals):

    lowSeen = vals[0]
    for i in range(0,len(vals)): 

        if vals[i]<lowSeen:
            lowSeen = vals[i]

        #add this to raise value error
        if vals[i]<0:
            raise ValueError("The number cannot be negative")





===============================================================
test set 3 test 2(finalized get lowest positive value function)
===============================================================
"""
def getLow(vals):

    lowSeen = vals[0]
    for i in range(0,len(vals)): 

        if vals[i]<lowSeen:
            lowSeen = vals[i]

        #add this to raise value error
        if vals[i]<0:
            raise ValueError("The number cannot be negative")

        #add this to raise type input error
        if type(vals[i]) not in [int,float]:
            raise TypeError("The input value must be positive interger or float")

    return lowSeen          













