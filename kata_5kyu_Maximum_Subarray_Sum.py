from collections import deque

def maxSequence(arr):
        
    d = deque(arr)         # convert the incoming list to a deque
    
    while d:               # get rid of all values < 1 that are on left & right edges
        if  d[0] < 1:
            d.popleft()
        elif d[-1] < 1:
            d.pop()
        else:
            break
            
    if  len(d) == 0: # covers cases of either all negs or initially empty list(arr)
        return 0

    max_tmp_tot = 0
    max_overall_tot = 0

# the following algorithm has a nested while loop. The inner while loop finds the maximum sum
# of the elements in deque tmp_Q by adding the values of the elements as they're popped from the
# left. It keeps a record of the current total of all element values, and of the highest that this
# total has been during the while loop. The outer while loop keeps a record of the highest total
# that the inner while loop found, and then removes (via popleft) the first element of the main
# deque (d) and runs the inner loop again. Once deque d is empty, we know we've tried all combos
# of consecutive "summed element values" and so we return the highest total found (in max_overall_tot)

    while d:
        t=0
        tmp_Q = deque(d)
        while tmp_Q:
            t = t + tmp_Q.popleft()
            if  t > max_tmp_tot:
                max_tmp_tot = t
        if  max_tmp_tot > max_overall_tot:
            max_overall_tot = max_tmp_tot
        d.popleft()

    print(d)
    print("max_tmp_tot",max_tmp_tot)
    print("max_overall_tot",max_overall_tot)
	
    return max_overall_tot

###########################

interesting alternative technique

def maxSequence_2(arr):
    s, temp = 0, 0
    for x in arr:
        temp += x
        temp = max(0, temp)
        s = max(s, temp)
    return s

#### TEST CASES ##########

test.describe("Tests")
test.it('should work on an empty array')   
test.assert_equals(maxSequence([]), 0)
test.it('should work on the example')
test.assert_equals(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
test.it('all negs example')
test.assert_equals(maxSequence([-2, -1, -3, -4, -1, -2, -1, -5, -4]), 0)
test.it('trim negs from both ends')
test.assert_equals(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, -4]), 6)


        
