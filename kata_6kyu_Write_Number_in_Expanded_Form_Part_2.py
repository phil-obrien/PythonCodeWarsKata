def expanded_form(n):
    z=""
    s=str(n)
    x=len(s)
    Units_Len = s.index(".")
    #Dec_Len = x-Units_Len-1
    Units_Mode=True # Units_Mode=True => digits being processed are prior to decimal point
    
    for i in range(0,x):
        if  s[i] == ".":
            Units_Mode=False
            continue
        if  s[i] != "0":
            if Units_Mode:
                z = z + s[i] + ("0" * (Units_Len-i-1)) + " + "  #"0" * (Units_Len-i-1) adds as many 0's
                                                                # as we need depending on where we 
                                                                # are in string (i) and on how many
                                                                # digits to left of dec point
            else:
                z = z + s[i] + "/1" + ("0" * ((i-Units_Len))) + " + "
                                                                #"0" * (i-Units_Len) adds as many
                                                                # zeroes as "i" is to-the-right
                                                                # of the decimal point
    
    #print(z[:-3])
    return z[:-3] # [:-3] ensures final " + " is trimmed off

print(expanded_form(1.24))    # expect: '1 + 2/10 + 4/100'
print(expanded_form(7.304))   # expect: '7 + 3/10 + 4/1000'
print(expanded_form(0.04))    # expect: '4/100'
print(expanded_form(123.456)) # expect: '100 + 20 + 3 + 4/10 + 5/100 + 6/1000'
