from collections import deque

# The fusc sequence (by Dijkstra), also known as Stern Brocot sequence can be described and sequenced
# as follows:
# The sequence starts with 0, 1. We can assume therefore that fusc(0) = 0 and fusc(1) = 1
#
# To get the next (third, or fusc(2)) number in the sequence, add fusc(0) to fusc(1) (0+1=1)
# Write 1 as the next number in the sequence, so the sequence is now 0, 1, 1
#
# To derive the rest of the numbers in the sequence, do as follows:
# Look at the next pair of numbers (1,1 is the next pair) and:
#  1) add them together (1+1=2) and write 2 as the next number in the sequence (seq = 0,1,1,2)
#  2) write the second number of the current pair (1) as the next number in the sequence (seq = 0,1,1,2,1)

# The next pair of numbers is (1,2) so (as above):
#  1) add them (1+2=3) and place 3 as the next number in the sequence (seq = 0,1,1,2,1,3)
#  2) write the second number of the current pair (2) as the next number in the sequence (seq = 0,1,1,2,1,3,2)

# The next pair of numbers is (2,1) so (as above):
#  1) add them (2+1=3) and place 3 as the next number in the sequence (seq = 0,1,1,2,1,3,2,3)
#  2) write the second number of the current pair (1) as the next number in the sequence (seq = 0,1,1,2,1,3,2,3,1)

# The next pair of numbers is (1,3) so (as above):
#  1) add them (1+3=4) and place 4 as the next number in the sequence (seq = 0,1,1,2,1,3,2,3,1,4)
#  2) write the second number of the current pair (3) as the next number in the sequence (seq = 0,1,1,2,1,3,2,3,1,4,3)

# ...and so on
# There's a very simple but useful video explaining the same thing here: https://www.youtube.com/watch?v=dbQVoilRKso
# The only thing to note is that the guide in the video starts with 1,1 (so doesn't include 0) but apart from that, it's the same

def fusc(n):
    #assert type(n) == int and n >= 0
    #Your code here
    
    if  n == 0 or n == 1: # we know fusc(0)=0 and fusc(1)=1 so if either is required, just return n
        return n
        
    dq = deque([1,1]) # No point including 0 as that has been covered by if statement above,
                      # plus subsequent steps are identical when starting from 1,1
    
    for i in range(1,n+1):
        x = dq.popleft()  # Chop off the leftmost value in the sequence (we won't be needing it in subsequent steps)
                          # x also represents the "left value in the pair"
        
        #print "x =",x, "(",i,")" # prints the value of fusc(n) and n itself!
        
        y = x + dq[0]    # Add the left value in the pair (i.e. "x") to the right value in the pair (which is now the first value in the deque) giving "y"
        dq.append(y)     # Add this total as the "next value in the sequence" (i.e. place it at the end of the deque)
        dq.append(dq[0]) # Now add the second number of the current pair next number in the sequence (also leaving it in place in the sequence as we'll need it in the next iteration of the loop) 
        
    return x # when n is reached by the for loop, whatever value is leftmost in the deque (or "x")
             # is the nth value in the sequence, i.e. fusc(n) so return that! Job done QED

"""
test.describe("The fusc function -- Part 1")
test.assert_equals(fusc(0), 0) 
test.assert_equals(fusc(1), 1)
test.assert_equals([fusc(i) for i in xrange(21)], [0, 1, 1, 2, 1, 3, 2, 3, 1, 4, 3, 5, 2, 5, 3, 4, 1, 5, 4, 7, 3])
test.assert_equals(fusc(85), 21)
"""

print("500000000...")    
print("500000000=", fusc(500000000)) #should print 3 as 3 is the fifth (starting from 0th) number in the sequence: 0, 1, 1, 2, 1, 3, 2, 3, 1, 4, 3, 5, 2, 5, 3, 4, 1, 5, 4, 7, 3
