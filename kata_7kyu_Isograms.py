def is_isogram(string):
  # Define a test_set as a SET of all the chars of an input string converted
  # to lower case. Converting to set ensures no duplicate elements are present.
  # After conversion if the lengths of string and SET are equal we know we are
  # dealing with an isogram
    
    test_set = set(string.lower())
    
    if  len(test_set) == len(string): 
        return True
    else:
        return False