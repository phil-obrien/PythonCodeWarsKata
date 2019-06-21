def validate_battlefield(field):

# First, do a generic check that no ship has been placed illegally by verifying diagonals
# basically the rule is that if any dot is diagonal to another, the placement is illegal

    for i in range(1,9):     # we don't need to parse edges as parsing diagonals of adjacent
        for j in range(1,9): #  rows/cols will cover this (hence use range 1,9 and not 0,10)
            if  field[i][j] == 1:
                if  field[i-1][j-1] == 1 \
                or  field[i+1][j+1] == 1 \
                or  field[i+1][j-1] == 1 \
                or  field[i-1][j+1] == 1:
                
                    return False
        
# Next, check that each ship required is present. We scan the map line by line
# and check each ship found to make sure the whole fleet is fully present and that there are no
# extra unwanted ships.
# Updating ship spaces from 1 to 2 means we've processed that spot

    tot_battleships = tot_cruisers = tot_destroyers = tot_subs = 0
    
# add a margin around the battlefield so we don't get index errors:
    for i in field:
        i.append(0)
    field.append([0,0,0,0,0,0,0,0,0,0,0])
    
    for i in range(0,10):
        for j in range(0,10):
            if  field[i][j] == 1:
                field[i][j] = 2
                if  field[i+1][j]==0 and field[i][j+1]==0: #we're processing a submarine
                    tot_subs+=1
                    if  tot_subs > 4: # too many submarines
                        for i in field: print(i)
                        #print("too many subs")
                        return False
                elif field[i+1][j]==1:
                    field[i+1][j]=2
                    if  field[i+2][j]==1:
                        field[i+2][j]=2
                        if  field[i+3][j]==1:
                            field[i+3][j]=2
                            tot_battleships += 1
                            if  tot_battleships > 1: # too many battleships
                                for i in field: print(i)
                                #print("too many battleships")
                                return False
                        else:
                            tot_cruisers += 1
                            if  tot_cruisers > 2: # too many cruisers
                                for i in field: print(i)
                                #print("too many cruisers")
                                return False
                    else:
                        tot_destroyers += 1
                        if  tot_destroyers > 3: # too many destroyers
                            for i in field: print(i)
                            #print("too many destroyers")
                            return False
                            
                else: # we know therefore that field[i][j+1]==1
                    field[i][j+1]=2
                    if  field[i][j+2]==1:
                        field[i][j+2]=2
                        if  field[i][j+3]==1:
                            field[i][j+3]=2
                            tot_battleships += 1
                            if  tot_battleships > 1: # too many battleships
                                for i in field: print(i)
                                #print("too many battleships")
                                return False
                        else:
                            tot_cruisers += 1
                            if  tot_cruisers > 2: # too many cruisers
                                for i in field: print(i)
                                #print("too many cruisers")
                                return False
                    else:
                        tot_destroyers += 1
                        if  tot_destroyers > 3: # too many destroyers
                            for i in field: print(i)
                            #print("too many destroyers")
                            return False
        
    if  tot_battleships == 1 \
    and tot_cruisers    == 2 \
    and tot_destroyers  == 3 \
    and tot_subs        == 4:
        return True
    else:
        #print(tot_subs,tot_destroyers,tot_cruisers,tot_battleships)
        return False

###################
from scipy.ndimage.measurements import label, find_objects, np
def validate_battlefield_2(field):
    field = np.array(field)
    return sorted(
        ship.size if min(ship.shape) == 1 else 0
        for ship in (field[pos] for pos in find_objects(label(field, np.ones((3,3)))[0]))
    ) == [1,1,1,1,2,2,2,3,3,4]


########################

    # fixed tests
    #Test.it("Fixed Tests")
    Test.it("Must return true for valid field")
    testfield = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    		     [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    		     [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
    		     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    		     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    		     [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    		     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    		     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    		     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    		     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    judge(testfield, True)
    
    Test.it("Must return false if unwanted ships are present")
    testfield = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    		     [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    		     [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
    		     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    		     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    	    	 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        		 [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    		     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    	    	 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    judge(testfield, False)
    
    Test.it("Must return false if number of ships of some type is incorrect")
    testfield = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    		     [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    		     [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
    		     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    		     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    		     [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
    		     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    		     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    		     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    		     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    judge(testfield, False)
    
    Test.it("Must return false if some of ships is missing")
    testfield = [[0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    		     [0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    		     [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
    		     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    		     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    		     [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    		     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    		     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    		     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    		     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    judge(testfield, False)
    
    Test.it("Must return false if ships are in contact")
    testfield = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    		     [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    		     [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
    		     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    		     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    		     [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    		     [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    		     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    		     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    		     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    judge(testfield, False)
    
    Test.it("Must return false if some of ships has incorrect shape (non-straight)")
    testfield = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    		     [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    		     [1, 1, 0, 0, 1, 1, 1, 0, 1, 0],
    		     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    		     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    		     [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    		     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    		     [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    		     [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    		     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    judge(testfield, False)
    		 
    Test.it("Must return false if the number and length of ships is not ok")
    testfield = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        		 [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    	    	 [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
    		     [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    		     [0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    		     [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    		     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    		     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    		     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    		     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    judge(testfield, False)


    # random tests
    Test.describe("Random Tests")
    for n in range(1, 101):
        test.it("Random #{}".format(n))
        testfield = buildCase()
        while not testfield:
            testfield = buildCase()
        judge(testfield)
    
tests()
