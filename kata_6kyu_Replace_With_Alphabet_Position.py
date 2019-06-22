def alphabet_position(text):
    alphabet=" abcdefghijklmnopqrstuvwxyz" # start with a space so a=1 rather than 0 (and so on!)
    number_string = ""
    
    for letter in text.lower():
        if  alphabet.find(letter) > 0:
            idx = alphabet.find(letter)
            number_string = number_string + str(idx) + " "
            
    return number_string.strip() # removes the trailing space (if there is one)
