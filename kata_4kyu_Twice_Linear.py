import time
import numpy as np

######## MY SOLUTION (not very fast - approx 22 seconds - this is too slow for codewars so I had to forfeit to see other solutions) ########

# Note - This was one of the first kata challenges I attempted on codewars, and the first where performance was relevant. Being still unaware of some of
#        of the "gems" to get faster Python code, I struggled to get good response times (eventually having to forfeit). I've placed my solution first,
#        then the solution provided by another user, and finally the "accepted" solution for this kata.
#
# Note - Short variable names were used as this actually sped up the code!
#

start=(time.time())

u=np.uint32([1])             # create a new numpy array called u and place the value 1 in it

for i in range(0,60000):     # we're going to have (not including duplicates!) at most 60,000 items in the numpy array - numpy arrays were used as they are meant to be faster than Python lists

    x=((u.item(i))*2)+1      # take the i-th item, multiply by 2 and add 1 (store result in x)
    y=((u.item(i))*3)+1      # take the i-th item, multiply by 3 and add 1 (store result in y)

    if x not in u:           # now try to add the double-and-add-1 to the numpy array!
        j = np.searchsorted(u,x,side='left') # j will be the index where x "slots" into the numpy array (using 'left' or 'right' for the side yields same index as x doesn't exist in u yet)
        u = np.insert(u,j,x) # inserts x into u at position j

    if y not in u:           # now try to add the triple-and-add-1 to the numpy array!
        j = np.searchsorted(u,y,side='left') # j will be the index where y "slots" into the numpy array (using 'left' or 'right' for the side yields same index as y doesn't exist in u yet)
        u = np.insert(u,j,y) # inserts y into u at position j

#print(u.item(20))

    
def dbl_linear(n):
    print(u)
    return u[n]

print(dbl_linear(60000))    # prints the 60,000th value in the numpy array

print ("My solution in seconds:",time.time() - start)

######## /MY SOLUTION (not very fast) ########


##############################################################################
##############################################################################
########## SOLUTION Provided by another codewards user (anon, sadly!)

def dbl_linear_3(n): ##seems incredibly fast - takes about 1 second
  u = [1]
  while len(u) < n*10:  # not sure why Anon uses n*10 but I guess it works! (I tried using n*5 instead and it halved the exec time, but n*10 is "safer" in case we run into loads of duplicates)
                        # n is the nth item in u (we're looking for this nth item).
                        # The only reason n needs to be bigger than len(u) is to accomodate duplicates while creating the list u
      u = set([y for x in u for y in (x, 2*x+1, 3*x+1)]) # uses set to eliminate duplicates from the list-comprehension being created
  return sorted(list(u))[n]

start_3=(time.time())

print(dbl_linear_3(60000)) # prints the 60,000th value

print ("Anon's solution in seconds:",time.time() - start_3)

#######################################
#######################################
#######################################
#kata official solution - fastest of what's here - takes about 0.1 seconds! 
#
# None of the code is mine, but I've commented it to clarify what's going on. This was one of the first kata I did (lacking Python experience back then!)
#
# The algorithm here uses 2 double-ended-queues from the COLLECTIONS module.
# The technique is simple and extremely fast. The value to be returned (we use h here) starts off
# as 1, and the formulae 2h+1, 3h+1 are applied to this 1, and appended to deques q2 and q3.
# Then we set h to be the lower of these two values (3 is lower than 4 so h becomes 3).
# 2 is then removed from q2 (and would have been removed from q3 as well had it been there) because we no longer need it.
# Add 1 to the counter to bring us one step closer to reaching the input parameter n.
# Next turn of the loop 2 goes thru formulae 2h+1 and 3h+1 and again the results are appended to the respective deques.
# When while counter (cnt) reaches n we have the value we need in h and so it is returned.
# Deques are extremely fast at processing values at each end, but slow at processing values in middle, so are ideal here.

from collections import deque

def dbl_linear_4(n):
    h = 1
    cnt = 0
    q2, q3 = deque([]), deque([]) # create 2 empty "double-ended-queues" (deque)
    while True:                   # keep executing until "return" breaks loop
        if (cnt >= n):            # really just means cnt = n (good practise to avoid infinite loops)
            return h
        q2.append(2 * h + 1)      # whatever h is, double and add 1 and stick it at the end of q2 deque
        q3.append(3 * h + 1)      # whatever h is, treble and add 1 and stick it at the end of q3 deque
        h = min(q2[0], q3[0])     # update h to be whatever is the lower of the first values in q2 and q3
        if  h == q2[0]:           # if h == first value in q2, "pop" first value in q2 into h (basically just remove first value from q2)
            h = q2.popleft()
        if  h == q3[0]:           # if h == first value in q3, "pop" first value in q3 into h (basically just remove first value from q3) 
            h = q3.popleft()       # doing the same thing for q2 and q3 ensure no duplicate values will be processed
        cnt += 1                  # bump counter cnt and start next loop cycle

start_4=(time.time())

print(dbl_linear_4(60000))

print ("'Accepted' solution in seconds:",time.time() - start_4)
