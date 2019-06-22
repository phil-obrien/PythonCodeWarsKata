def array_diff(a, b):

#function receives two lists, a and b. We want to remove ALL occurences
#of elements from a, which appear in b. 
    
    for i in b:             # for each element in list b...
        print("current element in list b:",i)
        try:                # (protect the execution with try as following remove() will cause exptn)
            while True:     # ...set up a loop to execute until an exception occurs...
                a.remove(i) # ...and now attempt to remove current element in b from list a...
        except:
            print("element not found - continue with next iteration of outer FOR")
            continue        # ...exeption raised when remove() doesn't find element in list a
                            # ...so then we continue with next iteration of FOR loop
    return a

#=====================================
#interesting alternative solution #1 (By Anon on Codewars)
def array_diff_1(a, b):

    return [x for x in a if x not in b] #pipo:list comprehension technique

#=====================================
#interesting alternative solution #2 (By Anon on Codewars)
def array_diff_2(a, b):
                                            #pipo:
    #return filter(lambda i: i not in b, a) #this only works in python2. In python3
                                            #this returns a filter object instead of
                                            #a list object

    #FILTER creates a list of elements for which a function returns true
    #the way it works is to use a function ("i not in b" in this case) and
    #APPLY that function to a list of elements (a is the list of elements)
    #In plain English, the line below is saying "give me all the i's where i
    #is in a but is not in b. If a=[3,4,5] and b=[4,5,6] the answer is 6
    #because it appears in a but does not appear in b. List comprehension is
    #clearer really (see 1st alt solution)

    return list(filter(lambda i: i not in b, a)) #Python3 code


#=====================================
#interesting alternative solution #3 (By Anon on Codewars)
def array_diff_3(a, b):

    for element in b:       #pipo: a similar solution to my own but neater
        while element in a:
            a.remove(element)
    return a

#=====================================
##MAIN PROGRAM:
print("my solution:",array_diff([3,4], [3]))

print("alt solution 1:",array_diff_1([3,4], [3]))

print("alt solution 2:",array_diff_2([3,4], [3]))

print("alt solution 3:",array_diff_3([3,4], [3]))

print("manual test:",list(filter(lambda i: i not in [3,4,5],[4,5,6])))
