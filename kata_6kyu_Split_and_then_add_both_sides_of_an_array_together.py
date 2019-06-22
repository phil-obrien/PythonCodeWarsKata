def split_and_add(numbers, n):
    print("numbers=",numbers)
    print("n=",n)
    
    print("length of numbers list =",len(numbers))
    
    if (n == 0) or (len(numbers) == 1): # if we started out with any "end-game" criteria then return immediately
        return numbers
    
    for loop_n_times in range(0,n):         # loop up to (but maybe less than!) n times
        a = list(numbers[:len(numbers)//2]) # a is the first "chunk" of the numbers list. It'll either be half, or half - 1 (dependant on len(numbers) being odd or even)
        b = list(numbers[len(numbers)//2:]) # b is the second "chunk" of the numbers list. It'll either be half, or half + 1 (dependant on len(numbers) being odd or even)

        print("a:",a)
        print("b:",b)

        numbers = []                        # blank out number list as we'll re-use this variable to define new list of numbers

        if  len(b) > len(a):                # if the second "chunk" has one more integer than the first "chunk", process the first integer of the second "chunk" alone
            numbers.append(b.pop(0))        # pop (remove) the first integer from b and place it in the currently empty numbers list. a and b are now equal length!
            print("numbers",numbers)

        for i in range(0,len(a)):           # for each integer in a...(and in b as it happens!)...
            numbers.append(a[i] + b[i])     # append the sum of corresponding integers in a and b and append them to numbers list
            print("numbers",numbers)
            
        if  len(numbers) == 1:              # if we're not finished looping according to n but we have narrowed numbers list down to one integer, it's time to return numbers!
            return numbers
            
    return numbers                          # we reach this point if main loop executed n times, so just return whatever we now have in numbers list
