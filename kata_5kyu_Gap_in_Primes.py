import math

def is_prime(test_num):
    """Check if t is prime. Return True if so, else False"""
    if test_num == 2:
        return True
    if test_num == 3:
        return True
    if test_num % 2 == 0:
        return False
    if test_num % 3 == 0:
        return False

    i = 5
    w = 2
    sqrt_test_num = math.sqrt(test_num)

    while i <= sqrt_test_num:     # once we reach the square root we know we're out of possibilities to find a divisor. Hence Prime = True
        if test_num % i == 0:
            return False

        i += w           # Intially w = 2. After adding 2 to i...
        w = 6 - w        # ...w is changed to be 4. In the next
                         # iteration of the while loop, w is switched
                         # back to 2 again. For each iteration, this same
                         # switch between 2 and 4 occurs, and the result added
                         # to i.
                         # This is a variant of the classic O(sqrt(N)) algorithm. 
                         # It uses the fact that a prime (except 2 and 3) is 
                         # of form 6k - 1 or 6k + 1 and looks only at divisors of this form
                         # Note! The code in this function is mostly not mine (borrowed from stackexchange and a couple of mods made by me)

    return True

def gap(g, m, n):
    print(g, m, n)
    
    inner_prime_found = False # Once we establish correct prime gap, we'll need to check if any primes exist in that gap!
    max = (n-g) + 1           # While searching for left prime, we only need to test up to range where left prime + gap would push us beyond limit (param n)
    
    for i in range(m,max):
        if  is_prime(i):
            if  is_prime(i+g):           # if True, we've found the right gap - next make sure there's no primes in the middle of that gap!
                inner_prime_found = False
                for j in range(i+1,i+g):
                    if  is_prime(j):
                        inner_prime_found = True
                        break # out of "for j" loop
                if  inner_prime_found:
                    continue  # go back out to next iteration the "for i" loop (as we've found the right gap but there was an inner prime ruining things!)
#                print(i,i+g)
                return [i,i+g]
                
    return None  # if we run out of primes in the range to check => no valid solution hence return None
    
