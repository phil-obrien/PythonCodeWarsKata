#define list of valid smilieys outside function to make processing faster
vs=[':)',':-)',':~)',';)',';-)',';~)',':D',':-D',':~D',';D',';-D',';~D']

def count_smileys(smiley_list):
    c=0
    for i in smiley_list:
        if  i in vs:  #add 1 to c whenever a valid smiley is found in the input list
            c+=1
   
    return c
############################
#Anon 1

#list comprehension and converting list to set
def count_smileys_2(arr):
    smiles = set([a+b+c for a in ":;" for b in ['','-', '~'] for c in ")D"])
    return len([1 for s in arr if s in smiles])

############################
#Anon 2

valid = ":) :D :-) :-D :~) :~D ;) ;D ;-) ;-D ;~) ;~D".split()

def count_smileys_3(arr):
    return sum(face in valid for face in arr)

############################
#Anon 3

#count_smileys=lambda a:sum(s and s[0]in':;'and s[-1]in')D'and s[1:-1]in('','-','~')for s in a)
