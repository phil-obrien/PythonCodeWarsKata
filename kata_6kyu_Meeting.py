def meeting(s):

    final_list = []
    return_string = ""

    initial_list = s.upper().split(";") # split incoming string into a list of (upper case)
                                        # strings, each one representing a name

    for i in initial_list:                  # for each name-string in the list, split out firstname 
        firstname, surname =  i.split(":")  # and surname, swap them, stick a comma in the middle
        final_list.append(surname + ", " + firstname) # and add the new string to another list
        
    final_list.sort() # sort the new list (the sort() function is an alphabetic sort here)
    
    for i in final_list:                # generate a new string made up of a concatenation of the
        return_string += "(" + i + ")"  # strings in final_list, plus surrounding parentheses
    
    return return_string
