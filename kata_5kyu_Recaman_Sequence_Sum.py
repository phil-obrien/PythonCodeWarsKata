import time

# Define two dicts and a set outside of the function so that the
# values in the dicts/set are retained between calls to the function
# This speeds up performance when testing function multiple times

d={0:0,1:0} #dict d holds n<->curr-val relationship (v)
e={0:0,1:0} #dict e holds n<->total-of-vals relationship (t)
s={0}       #set  s holds all v's which have been encountered

def rec(n):

    if  n in e:
        return e[n]

    i=max(d) # i is how far we got for n until now (FOR loop below will bring i up to n)
    v=d[i]   # v is the value of the nth number in the sequence 
    t=e[i]   # t is the total of all numbers in sequence up to and including n

    print("i:",i)
    print("v:",v)
    print("t:",t)

    for i in range(i,n):        # continue on with i's until we get to n-1
        if  v-i < 0 or v-i in s:  # if the current value minus where we are in the sequence <0 or has been seen already...
            v+=i                  # add i to v
        else:
            v-=i                  # else subtract i from v

        t+=v                      # update the running total of all v's found
        print("i:",i)
        print("v:",v)
        print("t:",t)
        d[i+1]=v                  # update the dictionary of n<->v's...
        e[i+1]=t                  # ...the dictionary of n<->t's...
        s.add(v)                  # ...and the set of all v's we have seen
        print("d:",d)
        print("e:",e)

    return t

start = time.time()

#print("return:",rec(2500000))
#print("return:",rec(4))
#print("return:",rec(3))
#print("return:",rec(4))
print("return:",rec(5))
print("return:",rec(9))
print("return:",rec(7))
#print("return:",rec(20))
print ((time.time() - start))

# n:   val  how    sum (val on this row + all prev vals)
# 1st = 0  (given) 0
# 2nd = 1  (0+1)   1
# 3rd = 3  (1+2)   4
# 4th = 6  (3+3)   10
# 5th = 2  (6-4)   12
# 6th = 7  (2+5)   19
# 7th = 13 (7+6)   32
# 8th = 20 (13+7)  52
# 9th = 12 (20-8)  64

# 0,1,3,6,2,7,13,20,12,21,11,22,10,23,9,24,8,25,43,62,42,63,41,18,42,17,43,
# 16,44,15,45,14,46,79,113,78,114,77,39,78,38,79,37,80,36,81,35,82,34,83,33,
# 84,32,85,31,86,30,87,29,88,28,89,27,90,26,91,157,224,156,225,155
