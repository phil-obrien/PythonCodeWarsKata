def countBits(n):

    """
    The requirement is to count the number of 1's in the binary version of decimal input n.
    In English, to work this out, you keep floor-dividing (ie truncate after decimal point)
    input n by 2 until n is 0. Before each floor-division, test the remainder of n divided
    by 2. If it's 1, increment the total number of 1's in the binary equivalent.
    Example: n is passed as 38:
    38 / 2 = 19 remainder 0
    19 / 2 = 9  remainder 1
     9 / 2 = 4  remainder 1
     4 / 2 = 2  remainder 0
     2 / 2 = 1  remainder 0
     1 / 2 = 0  remainder 1
    So the binary equivalent of 38 = 100110 (1x32 + 0x16 + 0x8 1x4 + 1x2 + 0x1)
    There are 3 1's in this binary number so 3 is returned from the function
    """
    total_ones = 0
        
    while n > 0:
        if  n % 2 == 1:      # does dividing n by 2 leave a remainder of 1?
            total_ones += 1  # if so add one to the total of 1's found
            
        n = n // 2           # update n to be the floor-division of itself divided by 2

    return total_ones

#################### Following solution by Anon on Codewars
def countBits_1(n):
    return bin(n).count("1") # alt solution which converts integer n to a binary 
                             # representation in STRING format using bin() function,
                             # and calculates the number of 1's using the count() function

print(countBits(38))
print(countBits(37))
print(countBits(33))
print(countBits(31))
print(countBits(128))
print(countBits(4))
print(countBits(2))
print(countBits(1))
print(countBits(0))
print(countBits(255))

print(countBits_1(38))
print(countBits_1(37))
print(countBits_1(33))
print(countBits_1(31))
print(countBits_1(128))
print(countBits_1(4))
print(countBits_1(2))
print(countBits_1(1))
print(countBits_1(0))
print(countBits_1(255))
