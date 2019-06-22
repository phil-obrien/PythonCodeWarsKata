import time

def recaman(n):

    if  n == 1:
        return 1 #this should really be 0 but the kata is incorrect I believe

    set_of_seen_numbers = {0}
    current_number = 0
    current_hop = 1
    number_of_hops_completed = 1

    while number_of_hops_completed < n+1: #this should really be n but the kata is incorrect I believe
        if  current_number - current_hop < 0:
            current_number += current_hop
        else:
            if (current_number - current_hop) in set_of_seen_numbers:
                current_number += current_hop
            else:
                current_number -= current_hop

        current_hop += 1
        set_of_seen_numbers.add(current_number)
        #print(current_number)
        number_of_hops_completed += 1

    return current_number

start = time.time()

print("my return (shortened variables):",recaman(2500000))

print((time.time() - start))


# 0,1,3,6,2,7,13,20,12,21,11,22,10,23,9,24,8,25,43,62,42,63,41,18,42,17,43,
# 16,44,15,45,14,46,79,113,78,114,77,39,78,38,79,37,80,36,81,35,82,34,83,33,
# 84,32,85,31,86,30,87,29,88,28,89,27,90,26,91,157,224,156,225,155
