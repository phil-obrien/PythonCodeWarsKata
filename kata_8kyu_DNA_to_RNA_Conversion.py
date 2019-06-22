def DNAtoRNA(dna):
    # create a function which returns an RNA sequence from the given DNA sequence
    
    while True:
        Thymine_here = dna.find("T")
        if  Thymine_here == -1:
            break #end the while loop
        else:
            print("Thymine_here",Thymine_here)
            dna = dna[0:Thymine_here] + "U" + dna[Thymine_here+1:]
            print("dna",dna)
    
    return dna

#best answer was STRING REPLACE function (Anon on Codewars)
def DNAtoRNA_2(dna):
    return dna.replace('T', 'U')

print(DNAtoRNA("GCATABC"))
