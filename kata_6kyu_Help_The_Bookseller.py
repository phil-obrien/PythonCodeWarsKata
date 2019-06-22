def stock_list(list_of_stock_codes, list_of_initial_chars)
    if  len(list_of_stock_codes) == 0 
    or  len(list_of_initial_chars) == 0
        return 
        
    return_string = 
    for single_char in list_of_initial_chars
        running_total = 0
        for code in list_of_stock_codes
            if  single_char == code[0]
                space_char_idx = code.index( )
                running_total += int(code[space_char_idx + 1])
        return_string = return_string + ( + single_char +    + str(running_total) + ) - 
    return return_string[-3] # knock off final  -  from end of string