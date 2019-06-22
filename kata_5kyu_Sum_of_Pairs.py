def sum_pairs(ints, s):

    ints2 = [] # ints2 will be identical to ints EXCEPT no duplicate value can appear more than twice
    left_val = right_val = None

    for i in ints:
        if  ints2.count(i) < 2: # ints2 will eliminate duplicate values after they've appeared more
            ints2.append(i)     # than twice, e.g. [1,1,1,2,2,3,1,2,4,3] becomes [1,1,2,2,3,4,3]

    len_ints2 = len(ints2)

    #print "ints2=", ints2, "s=",s

    earliest_index_of_2nd_pair_value = len_ints2 + 1 # set this to an impossibly high value initially

    for i in (range(len_ints2 - 1)):      # Loop thru all values except final value
        for j in (range(i+1,len_ints2)):  # Loop thru all remaining values incl. final value
            if  ints2[i] + ints2[j] == s: # If two values add to make total we're looking for...
                if  j < earliest_index_of_2nd_pair_value: # ...then if second value in pair is at a lower index than for any previous total found...
                    earliest_index_of_2nd_pair_value = j  # ..."remember" the index of the second value in pair...
                    left_val = ints2[i]                   # ...and also "remember" the two values totalling "s"
                    right_val = ints2[j]

    if  left_val == None: # if we didn't find a pair of values totalling the total we wanted...
        return None       # ..return None

    return [left_val,right_val]

print(sum_pairs([1, 4, 8, 7, 3, 15], 7))

"""
l1= [1, 4, 8, 7, 3, 15]
l2= [1, -2, 3, 0, -6, 1]
l3= [20, -13, 40]
l4= [1, 2, 3, 4, 1, 0]
l5= [10, 5, 2, 3, 7, 5]
l6= [4, -2, 3, 3, 4]
l7= [0, 2, 0]
l8= [5, 9, 13, -3]

test.describe("Testing For Sum of Pairs")
test.expect(sum_pairs(l1, 8) == [1, 7], "Basic: %s should return [1, 7] for sum = 8" % l1)
test.expect(sum_pairs(l2, -6) == [0, -6], "Negatives: %s should return [0, -6] for sum = -6" % l2)
test.expect(sum_pairs(l3, -7) == None, "No Match: %s should return None for sum = -7" % l3)
test.expect(sum_pairs(l4, 2) == [1, 1], "First Match From Left: %s should return [1, 1] for sum = 2 " % l4)
test.expect(sum_pairs(l5, 10) == [3, 7], "First Match From Left REDUX!: %s should return [3, 7] for sum = 10 " % l5)
test.expect(sum_pairs(l6, 8) == [4, 4], "Duplicates: %s should return [4, 4] for sum = 8" % l6)
test.expect(sum_pairs(l7, 0) == [0, 0], "Zeroes: %s should return [0, 0] for sum = 0" % l7)
test.expect(sum_pairs(l8, 10) == [13, -3], "Subtraction: %s should return [13, -3] for sum = 10" % l8)

"""
