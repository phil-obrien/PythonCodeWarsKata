# -- coding utf-8 --
def dative(word)
    front_vowel = ['e', 'é', 'i', 'í', 'ö', 'ő', 'ü', 'ű']
    back_vowel = ['a', 'á', 'o', 'ó', 'u', 'ú']
    for i in word[-1] # [-1] means startfinishstep and step is -1 hence string is read in reverse
        if  i in front_vowel
            return word + nek
        elif i in back_vowel
            return word + nak