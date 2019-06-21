def mix(s1, s2):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    list_strings_sorted_alpha = []
    list_strings_sorted_length_and_alpha = []
    
    for letter in alphabet:
        s1_total = s1.count(letter)
        s2_total = s2.count(letter)
        
        if  s1_total > 1 or s2_total > 1:
            if  s1_total > s2_total:
                bigger_count = '1'
                multiplier = s1_total
            elif s1_total < s2_total:
                bigger_count = '2'
                multiplier = s2_total
            else:
                bigger_count = '='
                multiplier = s1_total # s1_total and s1_total are the same so either will do
            
            tmp_string = bigger_count + ':' + (letter * multiplier) # tmp_string will begin with either '1','2' or '=' respectively, which handily are in 'ascending' order
            list_strings_sorted_alpha.append(tmp_string)

    if  len(list_strings_sorted_alpha) == 0: # return an empty string if no char was found more than once in either string
        return ""

    # we need to sort the list because we generated it based on the alphabet then added 1:/2:/=: hence we may have something like ['=:aaa', '2:bb', '1:ccc', '2:ddd','=ee']...
    #  ...whereas what we need is all 1's then all 2's then all ='s (on an ORDERED BY LENGTH basis but that comes later) e.g. ['1:ccc','2:bb','2=:ddd','=:aaa','=:ee']
    #  ...i.e. the strings should be sorted by 1 / 2 / = (and within that, on length, but the length-sort comes later!)
    list_strings_sorted_alpha.sort()
    print(list_strings_sorted_alpha)
    
    # the following line finds the length of the longest string in the list (not the longest string itself, just the length of it!)
    max_string_length_in_list = len(max(list_strings_sorted_alpha, key=len))
    
    # The following for loop creates a list sorted on length (retaining alphabetic sort already done).
    # It works by working downwards from the length of the longest string, finding all strings of that length, adding all of those to the new list, and then 
    # checking for the next shortest string, etc, until and including length = 4 (4 because shortest string must be in format 1:aa for example. 1:a is not required)
    for find_strings_of_length in range(max_string_length_in_list,3,-1):
        for string_item in list_strings_sorted_alpha:
            if  len(string_item) == find_strings_of_length:
                list_strings_sorted_length_and_alpha.append(string_item)

    # lastly we form one long string by 'join'ing the individual strings of the list together, separated by '/'
    final_string = "/".join(list_strings_sorted_length_and_alpha)
    print("final_string",final_string)
    return final_string
