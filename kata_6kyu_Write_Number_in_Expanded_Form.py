def expanded_form(n):
    z=""
    s=str(n)
    x=len(s)
    for i in range(0,x):
        if  s[i] != "0":
            z = z + s[i] + ("0" * (x-i-1)) + " + "  #"0" * (x-i-1) adds as many 0's as we need
                                                    # depending on where we are in string (i) and
                                                    # on how long the original string was (x)

    return z[:-3] # [:-3] ensures final " + " is trimmed off

#######################
# Anon codewars user
def expanded_form_2(num):
    return ' + '.join([a+'0'*b for b, a in zip(reversed(range(len(str(num)))), str(num)) if a not in '0'])

#NOTE - difference in how zip function behaves in Python 2 v 3

#######################
# Anon codewars user
def expanded_form_3(num):
    num = str(num)
    return ' + '.join([num[i] + '0' * (len(num) - 1 - i) for i in range(len(num)) if num[i] != '0'])

#######################
print(expanded_form(12))    #expect: '10 + 2'
print(expanded_form(42))    #expect: '40 + 2'
print(expanded_form(70304)) #expect: '70000 + 300 + 4'
