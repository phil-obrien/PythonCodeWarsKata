def solution(list_in):

    consecutive_list = []   # this holds temporary lists of consecutive values as the main input list_in is iterated through
    out_string = ""         # this is the string that will be returned
    
    consecutive_list.append(list_in.pop(0)) # remove'the first value from the input list_in and place it in the temp consecutive_list
    
    for i in list_in:
        if  i == (consecutive_list[-1] + 1): # if the next value in list_in is consecutive to the last value in consecutive_list...
            consecutive_list.append(i)       #  ...append it to consecutive_list
            
        else:                                # When the next value in list_in is NOT consecutive to the last value in consecutive_list we must process the values in consecutive_list.
            if  len(consecutive_list) > 2:   # If we have more than 2 values in consecutive_list it means we must add to output_string in the a-z format
                out_string = out_string + str(consecutive_list[0]) + "-" + str(consecutive_list[-1]) + ","
                consecutive_list = [i]       # Now re-initialise consecutive_list so it contains only the non-consecutive value we found in list_in
            else:
                for j in consecutive_list:   # If we have less than 3 values in consecutive_list it means we must add to output string in the x,y format
                    out_string = out_string + str(j) + "," # Use a for loop to iterate the either 1 or 2 values in consecutive_list (we end up with either x,y, or x,)
                    consecutive_list = [i]

    if  len(consecutive_list) < 3:  # Once the main loop has completed on list_in, it's possible that there are value(s) still in consecutive_list
        for i in consecutive_list:  # If there are less than 3 values (0, 1 or 2) loop through them and output in format x,y
            out_string = out_string + str(i) + ","
    else:                           # If there are 3 or more values in consecutive_list then output in format a-z
        out_string = out_string + str(consecutive_list[0]) + "-" + str(consecutive_list[-1])

    if  out_string[-1] == ',':         # If the last character of the out_string is a comma...
        out_string = out_string[:-1]   # ...shave it off!
    
    return out_string
