import numpy as np
import time
#from collections import deque

# This coding solution needs a detailed explanation. Please insert that here at the top!

#**********************************
def no_trapped_segments():
#**********************************

    def blocked_4_ways():

        blocked = 0
        
        #check left
        if  y == 0:
            blocked += 1
        else:
            if  a[x,y-1] != -1:
                blocked += 1

        #check right
        if  y == 4:
            blocked += 1
        else:
            if  a[x,y+1] != -1:
                blocked += 1

        #check above
        if  x == 0:
            blocked += 1
        else:
            if  a[x-1,y] != -1:
                blocked += 1

        #check below
        if  x == 4:
            blocked += 1
        else:
            if  a[x+1,y] != -1:
                blocked += 1

        #print(blocked)
        return (blocked == 4)
                
    pos = np.argmin(a) # pos will be first occurence of -1 in array a
    x, y = pos_to_array_coords(pos)

    for j in range(y,5): # check the rest of the row we're on
        if  a[x,y] == -1 and blocked_4_ways():
            return False

    for i in range(x+1,5):
        for j in range(0,5):
            if  a[x,y] == -1 and blocked_4_ways():
                return False

    return True

#**********************************
def pos_to_array_coords(position):
#**********************************

    p = (time.time())

    row = position//5
    col = position%5

    q = time.time() - p
    global s
    s += q

    return(row,col)

#*****************************************************
def position_valid(digit, try_row, try_col):
#*****************************************************

    # We need an equivalent digit somewhere orthagonal of where we are:

    #check left
    if  try_col == 0:
        pass
    else:
        if (a[try_row, try_col-1] == digit):
            return True

    #check above
    if  try_row == 0:
        pass
    else:
        if (a[try_row-1, try_col] == digit):
            return True

    #check right
    if  try_col == 4:
        pass
    else:
        if (a[try_row, try_col+1] == digit):
            return True

    #check below
    if  try_row == 4:
        pass
    else:
        if (a[try_row+1, try_col] == digit):
            return True

    return False # can't place this digit here!

#############################
def process_DISTRICT_0():
#############################

    global a
    global b
    global m
    global n

    #print("dst 0 code here")

    a[0,0] = 0 # Anchor position of District 0 (Segment 0) is position 0 (coords 0,0). This will never change
    m[0,0] = 0 # The m-emorised position of d0s0 is also 0

    b[0]=np.array(a)
    n[0]=np.array(m)
    #############################
    for d0s1 in (1,5): # District 0 Segment 1 can only be in positions 1 or 5
        #print("loop through possibilities for District 0 Segment 1")

        if  m[0,1] != -1: # dist 0 seg 1 = [0]
            a=np.array(b[0])
            m=np.array(n[0])

        new_row, new_col = pos_to_array_coords(d0s1) # translate position to coords

        if  a[new_row,new_col] == -1: # ...if nothing there yet
            if  position_valid(0,new_row,new_col): # ...if there is a "0" orthagonally adjacent to where we are
                a[new_row,new_col] = 0
                m[0,1] = d0s1     # Update the m-emorised position of this segment
                b[1]=np.array(a)  # Backup a
                n[1]=np.array(m)  # Backup m

                #############################
                for d0s2 in range(d0s1,12): # loop through possibilities for District 0 Segment 2. Range up to 11 as this seg can never go further
                    #print("loop through possibilities for District 0 Segment 2")

                    if  m[0,2] != -1: # dist 0 seg 2 = [1]
                        a=np.array(b[1])
                        m=np.array(n[1])

                    new_row, new_col = pos_to_array_coords(d0s2) # translate position to coords
                    if  a[new_row,new_col] == -1: # ...if nothing there yet
                        if  position_valid(0,new_row,new_col): # ...if there is a "0" orthagonally adjacent to where we are
                            a[new_row,new_col] = 0
                            m[0,2] = d0s2    # Update the m-emorised position of this segment
                            b[2]=np.array(a)  # Backup a
                            n[2]=np.array(m)  # Backup m

                            #############################
                            for d0s3 in range(d0s2,16): # loop through possibilities for District 0 Segment 3. Range up to 15 as this seg can never go further
                                #print("loop through possibilities for District 0 Segment 3")

                                if  m[0,3] != -1: # dist 0 seg 3 = [2]
                                    a=np.array(b[2])
                                    m=np.array(n[2])

                                new_row, new_col = pos_to_array_coords(d0s3) # translate position to coords
                                if  a[new_row,new_col] == -1: # ...if nothing there yet
                                    if  position_valid(0,new_row,new_col): # ...if there is a "0" orthagonally adjacent to where we are
                                        a[new_row,new_col] = 0
                                        m[0,3] = d0s3        # Update the m-emorised position of this segment
                                        b[3]=np.array(a)  # Backup a
                                        n[3]=np.array(m)  # Backup m

                                        #############################
                                        for d0s4 in range(d0s3,22): # loop through possibilities for District 0 Segment 4
                                            #print("loop through possibilities for District 0 Segment 4")

                                            if  m[0,4] != -1:
                                                a=np.array(b[3])
                                                m=np.array(n[3])

                                            new_row, new_col = pos_to_array_coords(d0s4) # translate position to coords
                                            if  a[new_row,new_col] == -1: # ...if nothing there yet
                                                if  position_valid(0,new_row,new_col): # ...if there is a "0" orthagonally adjacent to where we are
                                                    a[new_row,new_col] = 0
                                                    m[0,4] = d0s4        # Update the m-emorised position of this segment
                                                    b[4]=np.array(a)  # Backup a
                                                    n[4]=np.array(m)  # Backup m

                                                    process_DISTRICT_1()
                                                    #global count
                                                    #count += 1
                                                    #print(count)
                                                    #print(a)
                                                    #print(m)

                                                    #return


#############################
def process_DISTRICT_1():
#############################

    global a
    global b
    global m
    global n

    # blank out memorised combos of 1's, as we have a new combo of 0's to work with now!
    d1_combo_history = []


    for d1s0 in range(np.argmin(a),6): # we can trim down the FOR loop as we know only 5 0's have been placed so far!
        #print("District 1 Segment 0 is an ANCHOR position. It's more mobile than D0S0 anchor as it is placed in first available free position")

        if  m[1,0] != -1:
            a=np.array(b[4])
            m=np.array(n[4])

        new_row, new_col = pos_to_array_coords(d1s0) # translate position to coords
        if  a[new_row,new_col] == -1: # ...if nothing there yet
            a[new_row,new_col] = 1
            m[1,0] = d1s0        # Update the m-emorised position of this segment
            b[5]=np.array(a)  # Backup a
            n[5]=np.array(m)  # Backup m

            break #out of current FOR loop (d1s0) as soon as we've found valid spot for d1s0


    #############################

    for d1s1 in range(np.argmin(a),11): # loop through possibilities for District 1 Segment 1 (can only be at max in pos 10)
        #print("loop through possibilities for District 1 Segment 1")

        if  m[1,1] != -1:
            a=np.array(b[5])
            m=np.array(n[5])

        new_row, new_col = pos_to_array_coords(d1s1) # translate position to coords
        if  a[new_row,new_col] == -1: # ...if nothing there yet
            if  position_valid(1,new_row,new_col): # ...if there is a "1" orthagonally adjacent to where we are
                a[new_row,new_col] = 1
                m[1,1] = d1s1     # Update the m-emorised position of this segment
                b[6]=np.array(a)  # Backup a
                n[6]=np.array(m)  # Backup m

                #############################

                for d1s2 in range(np.argmin(a),16): # loop through possibilities for District 1 Segment 2 (can only be at max in pos 15)
                    #print("loop through possibilities for District 1 Segment 2")

                    if  m[1,2] != -1:
                        a=np.array(b[6])
                        m=np.array(n[6])

                    new_row, new_col = pos_to_array_coords(d1s2) # translate position to coords
                    if  a[new_row,new_col] == -1: # ...if nothing there yet
                        if  position_valid(1,new_row,new_col): # ...if there is a "1" orthagonally adjacent to where we are
                            a[new_row,new_col] = 1
                            m[1,2] = d1s2     # Update the m-emorised position of this segment
                            b[7]=np.array(a)  # Backup a
                            n[7]=np.array(m)  # Backup m

                            #############################

                            for d1s3 in range(np.argmin(a),21): # loop through possibilities for District 1 Segment 3 (can only be at max in pos 20)
                                #print("loop through possibilities for District 1 Segment 3")

                                if  m[1,3] != -1:
                                    a=np.array(b[7])
                                    m=np.array(n[7])

                                new_row, new_col = pos_to_array_coords(d1s3) # translate position to coords
                                if  a[new_row,new_col] == -1: # ...if nothing there yet
                                    if  position_valid(1,new_row,new_col): # ...if there is a "1" orthagonally adjacent to where we are
                                        a[new_row,new_col] = 1
                                        m[1,3] = d1s3     # Update the m-emorised position of this segment
                                        b[8]=np.array(a)  # Backup a
                                        n[8]=np.array(m)  # Backup m

                                        #############################

                                        for d1s4 in range(np.argmin(a),25): # loop through possibilities for District 1 Segment 4
                                            #print("loop through possibilities for District 1 Segment 4")

                                            if  m[1,4] != -1:
                                                a=np.array(b[8])
                                                m=np.array(n[8])

                                            new_row, new_col = pos_to_array_coords(d1s4) # translate position to coords
                                            if  a[new_row,new_col] == -1: # ...if nothing there yet
                                                if  position_valid(1,new_row,new_col): # ...if there is a "1" orthagonally adjacent to where we are
                                                    a[new_row,new_col] = 1
                                                    m[1,4] = d1s4     # Update the m-emorised position of this segment
                                                    b[9]=np.array(a)  # Backup a
                                                    n[9]=np.array(m)  # Backup m

                                                    # We now have our 5 candidate positions for the 5 segments in District-1. We need to make sure that we haven't
                                                    # had the same combination of 1's in the same positions (it doesn't matter which 1 goes where, only that the five 1's
                                                    # ended up occupying the same 5 positions in the array.
                                                    # Check the stored combos: If not found, add it and move on to next District.
                                                    # If combo found, don't move on to next District. Instead, keep searching for combos of 1's until we find one we haven't
                                                    #  used before.

                                                    temp_list = list(m[1,])
                                                    temp_list.sort()

                                                    if  temp_list not in d1_combo_history:
                                                        d1_combo_history.append(temp_list)

                                                        #global count
                                                        #count += 1

                                                        #print(count)
                                                        #print(a)
                                                        #print(m)

                                                        #if  no_trapped_segments():
                                                        process_DISTRICT_2()
                                                        #else:
                                                        #    print(a)
                                                    #return

#############################
def process_DISTRICT_2():
#############################

    global a
    global b
    global m
    global n

    # blank out memorised combos of 2's, as we have a new combo of 1's to work with now!
    d2_combo_history = []

    for d2s0 in range(np.argmin(a),25):
        #print("District 2 Segment 0 is an ANCHOR position.")

        if  m[2,0] != -1:
            a=np.array(b[9])
            m=np.array(n[9])

        new_row, new_col = pos_to_array_coords(d2s0) # translate position to coords
        if  a[new_row,new_col] == -1: # ...if nothing there yet
            a[new_row,new_col] = 2
            m[2,0] = d2s0        # Update the m-emorised position of this segment
            b[10]=np.array(a)  # Backup a
            n[10]=np.array(m)  # Backup m

            break #out of current FOR loop (d2s0) as soon as we've found valid spot for d2s0


    #############################

    for d2s1 in range(np.argmin(a),25): # loop through possibilities for District 2 Segment 1
        #print("loop through possibilities for District 2 Segment 1")

        if  m[2,1] != -1:
            a=np.array(b[10])
            m=np.array(n[10])

        new_row, new_col = pos_to_array_coords(d2s1) # translate position to coords
        if  a[new_row,new_col] == -1: # ...if nothing there yet
            if  position_valid(2,new_row,new_col): # ...if there is a "2" orthagonally adjacent to where we are
                a[new_row,new_col] = 2
                m[2,1] = d2s1     # Update the m-emorised position of this segment
                b[11]=np.array(a)  # Backup a
                n[11]=np.array(m)  # Backup m

                #############################

                for d2s2 in range(np.argmin(a),25): # loop through possibilities for District 2 Segment 2
                    #print("loop through possibilities for District 2 Segment 2")

                    if  m[2,2] != -1:
                        a=np.array(b[11])
                        m=np.array(n[11])

                    new_row, new_col = pos_to_array_coords(d2s2) # translate position to coords
                    if  a[new_row,new_col] == -1: # ...if nothing there yet
                        if  position_valid(2,new_row,new_col): # ...if there is a "2" orthagonally adjacent to where we are
                            a[new_row,new_col] = 2
                            m[2,2] = d2s2     # Update the m-emorised position of this segment
                            b[12]=np.array(a)  # Backup a
                            n[12]=np.array(m)  # Backup m

                            #############################

                            for d2s3 in range(np.argmin(a),25): # loop through possibilities for District 2 Segment 3
                                #print("loop through possibilities for District 2 Segment 3")

                                if  m[2,3] != -1:
                                    a=np.array(b[12])
                                    m=np.array(n[12])

                                new_row, new_col = pos_to_array_coords(d2s3) # translate position to coords
                                if  a[new_row,new_col] == -1: # ...if nothing there yet
                                    if  position_valid(2,new_row,new_col): # ...if there is a "2" orthagonally adjacent to where we are
                                        a[new_row,new_col] = 2
                                        m[2,3] = d2s3     # Update the m-emorised position of this segment
                                        b[13]=np.array(a)  # Backup a
                                        n[13]=np.array(m)  # Backup m

                                        #############################

                                        for d2s4 in range(np.argmin(a),25): # loop through possibilities for District 2 Segment 4
                                            #print("loop through possibilities for District 2 Segment 4")

                                            if  m[2,4] != -1:
                                                a=np.array(b[13])
                                                m=np.array(n[13])

                                            new_row, new_col = pos_to_array_coords(d2s4) # translate position to coords
                                            if  a[new_row,new_col] == -1: # ...if nothing there yet
                                                if  position_valid(2,new_row,new_col): # ...if there is a "2" orthagonally adjacent to where we are
                                                    a[new_row,new_col] = 2
                                                    m[2,4] = d2s4     # Update the m-emorised position of this segment
                                                    b[14]=np.array(a)  # Backup a
                                                    n[14]=np.array(m)  # Backup m

                                                    # We now have our 5 candidate positions for the 5 segments in District-2. We need to make sure that we haven't
                                                    # had the same combination of 2's in the same positions (it doesn't matter which 2 goes where, only that the five 2's
                                                    # ended up occupying the same 5 positions in the array.
                                                    # Check the stored combos: If not found, add it and move on to next District.
                                                    # If combo found, don't move on to next District. Instead, keep searching for combos of 2's until we find one we haven't
                                                    #  used before.

                                                    temp_list = list(m[2,])
                                                    temp_list.sort()

                                                    if  temp_list not in d2_combo_history:
                                                        d2_combo_history.append(temp_list)

                                                        #global count
                                                        #count += 1

                                                        #print(count)
                                                        #print("a\n",a)
                                                        #print("m\n",m)
                                                        #if  no_trapped_segments():
                                                        process_DISTRICT_3()
                                                    #return


#############################
def process_DISTRICT_3():
#############################

    global a
    global b
    global m
    global n

    # blank out memorised combos of 3's, as we have a new combo of 2's to work with now!
    d3_combo_history = []

    for d3s0 in range(np.argmin(a),25):
        #print("District 3 Segment 0 is an ANCHOR position.")

        if  m[3,0] != -1:
            a=np.array(b[14])
            m=np.array(n[14])

        new_row, new_col = pos_to_array_coords(d3s0) # translate position to coords
        if  a[new_row,new_col] == -1: # ...if nothing there yet
            a[new_row,new_col] = 3
            m[3,0] = d3s0        # Update the m-emorised position of this segment
            b[15]=np.array(a)  # Backup a
            n[15]=np.array(m)  # Backup m

            break #out of current FOR loop (d3s0) as soon as we've found valid spot for d3s0


    #############################

    for d3s1 in range(np.argmin(a),25): # loop through possibilities for District 3 Segment 1
        #print("loop through possibilities for District 3 Segment 1")

        if  m[3,1] != -1:
            a=np.array(b[15])
            m=np.array(n[15])

        new_row, new_col = pos_to_array_coords(d3s1) # translate position to coords
        if  a[new_row,new_col] == -1: # ...if nothing there yet
            if  position_valid(3,new_row,new_col): # ...if there is a "3" orthagonally adjacent to where we are
                a[new_row,new_col] = 3
                m[3,1] = d3s1     # Update the m-emorised position of this segment
                b[16]=np.array(a)  # Backup a
                n[16]=np.array(m)  # Backup m

                #############################

                for d3s2 in range(np.argmin(a),25): # loop through possibilities for District 3 Segment 2
                    #print("loop through possibilities for District 3 Segment 2")

                    if  m[3,2] != -1:
                        a=np.array(b[16])
                        m=np.array(n[16])

                    new_row, new_col = pos_to_array_coords(d3s2) # translate position to coords
                    if  a[new_row,new_col] == -1: # ...if nothing there yet
                        if  position_valid(3,new_row,new_col): # ...if there is a "3" orthagonally adjacent to where we are
                            a[new_row,new_col] = 3
                            m[3,2] = d3s2     # Update the m-emorised position of this segment
                            b[17]=np.array(a)  # Backup a
                            n[17]=np.array(m)  # Backup m

                            #############################

                            for d3s3 in range(np.argmin(a),25): # loop through possibilities for District 3 Segment 3
                                #print("loop through possibilities for District 3 Segment 3")

                                if  m[3,3] != -1:
                                    a=np.array(b[17])
                                    m=np.array(n[17])

                                new_row, new_col = pos_to_array_coords(d3s3) # translate position to coords
                                if  a[new_row,new_col] == -1: # ...if nothing there yet
                                    if  position_valid(3,new_row,new_col): # ...if there is a "3" orthagonally adjacent to where we are
                                        a[new_row,new_col] = 3
                                        m[3,3] = d3s3     # Update the m-emorised position of this segment
                                        b[18]=np.array(a)  # Backup a
                                        n[18]=np.array(m)  # Backup m

                                        #############################

                                        for d3s4 in range(np.argmin(a),25): # loop through possibilities for District 3 Segment 4
                                            #print("loop through possibilities for District 3 Segment 4")

                                            if  m[3,4] != -1:
                                                a=np.array(b[18])
                                                m=np.array(n[18])

                                            new_row, new_col = pos_to_array_coords(d3s4) # translate position to coords
                                            if  a[new_row,new_col] == -1: # ...if nothing there yet
                                                if  position_valid(3,new_row,new_col): # ...if there is a "3" orthagonally adjacent to where we are
                                                    a[new_row,new_col] = 3
                                                    m[3,4] = d3s4     # Update the m-emorised position of this segment

                                                    # We now have our 5 candidate positions for the 5 segments in District-3. We need to make sure that we haven't
                                                    # had the same combination of 3's in the same positions (it doesn't matter which 3 goes where, only that the five 3's
                                                    # ended up occupying the same 5 positions in the array.
                                                    # Check the stored combos: If not found, add it and move on to next District.
                                                    # If combo found, don't move on to next District. Instead, keep searching for combos of 3's until we find one we haven't
                                                    #  used before.

                                                    temp_list = list(m[3,])
                                                    temp_list.sort()

                                                    if  temp_list not in d3_combo_history:
                                                        d3_combo_history.append(temp_list)

##                                                        global count
##                                                        count += 1

##                                                        print(count)
##                                                        print("a\n",a)
##                                                        print("m\n",m)

                                                        process_DISTRICT_4()
                                                    #return


#############################
def process_DISTRICT_4():
#############################

    global a
    global b
    global m
    global n

    # District 4 Segment 0 (this can go in the first available space on the board)

    #print("*********** entering D4 processing ************")

    d4sx = np.argmin(a)
    new_row, new_col = pos_to_array_coords(d4sx) # translate position to coords
    a[new_row,new_col] = 4
    m[4,0] = d4sx

    # District 4 Segment 1 (from now on segments must be valid, i.e. orthagonally adjacent to another "4")

    for d4sx in range(np.argmin(a),25):
        new_row, new_col = pos_to_array_coords(d4sx) # translate position to coords
        if  a[new_row,new_col] == -1:
            if  position_valid(4,new_row,new_col): # ...if there is a "4" orthagonally adjacent to where we are
                a[new_row,new_col] = 4
                m[4,1] = d4sx
                break # move on to the next segment
            elif d4sx == 24:
                return # go back to D3S4 "for loop" logic (where we will look for next valid last-seg of dst 3)
        elif d4sx == 24: # we get here if we've passed through all spaces and can't find valid place to put this segment
            return # go back to D3S4 "for loop" logic (where we will look for next valid last-seg of dst 3)


    # District 4 Segment 2 (from now on segments must be valid, i.e. orthagonally adjacent to another "4")

    for d4sx in range(np.argmin(a),25):
        new_row, new_col = pos_to_array_coords(d4sx) # translate position to coords
        if  a[new_row,new_col] == -1:
            if  position_valid(4,new_row,new_col): # ...if there is a "4" orthagonally adjacent to where we are
                a[new_row,new_col] = 4
                m[4,2] = d4sx
                break # move on to the next segment
            elif d4sx == 24:
                return # go back to D3S4 "for loop" logic (where we will look for next valid last-seg of dst 3)
        elif d4sx == 24: # we get here if we've passed through all spaces and can't find valid place to put this segment
            return # go back to D3S4 "for loop" logic (where we will look for next valid last-seg of dst 3)

    # District 4 Segment 3 (from now on segments must be valid, i.e. orthagonally adjacent to another "4")

    for d4sx in range(np.argmin(a),25):
        new_row, new_col = pos_to_array_coords(d4sx) # translate position to coords
        if  a[new_row,new_col] == -1:
            if  position_valid(4,new_row,new_col): # ...if there is a "4" orthagonally adjacent to where we are
                a[new_row,new_col] = 4
                m[4,3] = d4sx
                break # move on to the next segment
            elif d4sx == 24:
                return # go back to D3S4 "for loop" logic (where we will look for next valid last-seg of dst 3)
        elif d4sx == 24: # we get here if we've passed through all spaces and can't find valid place to put this segment
            return # go back to D3S4 "for loop" logic (where we will look for next valid last-seg of dst 3)

    # District 4 Segment 4 (from now on segments must be valid, i.e. orthagonally adjacent to another "4")

    for d4sx in range(np.argmin(a),25):
        new_row, new_col = pos_to_array_coords(d4sx) # translate position to coords
        if  a[new_row,new_col] == -1:
            if  position_valid(4,new_row,new_col): # ...if there is a "4" orthagonally adjacent to where we are
                a[new_row,new_col] = 4
                m[4,4] = d4sx
                break # move on to the next segment
            elif d4sx == 24:
                return # go back to D3S4 "for loop" logic (where we will look for next valid last-seg of dst 3)
        elif d4sx == 24: # we get here if we've passed through all spaces and can't find valid place to put this segment
            return # go back to D3S4 "for loop" logic (where we will look for next valid last-seg of dst 3)

    global count
    count += 1

    global dq
    dq.append(list(a[0,]) + list(a[1,]) +list(a[2,]) +list(a[3,]) +list(a[4,]))

##    if  count > 3990 or count < 10:
##        print("count:",count)
##        print("a\n",a)
##        print("m\n",m)


#*****************************
# MAIN PROGRAM
#*****************************
start_time = (time.time())

a = np.full((5, 5), -1, np.int8) # this is our "map". -1 means a free space. 0-4 inclusive are district numbers

m = np.full((5, 5), -1, np.int8) # this 5x5 array starts off full of -1's. The elements will "remember" where
                                    # each segment of each district currently lies.
                                    # -1 means it isn't allocated yet (or has been deallocated).

b = np.full((19, 5, 5), -1, np.int8)  # Backups for a so we can easily revert to earlier version of a
n = np.full((19, 5, 5), -1, np.int8)  # Backups for m so we can easily revert to earlier version of m

s = 0 # count for loop in translate pos to coords


dq = []
##dq = deque([])

count = 0

process_DISTRICT_0()

##print("list",len(dq))

#print("final array\n", a)
print("count = ",count)

print (time.time() - start_time)
print("pos2coords time = ",s)



def gerrymander(s):

    s=s.replace("\n","")
    print(s)
    
    final_list = []
    d=[0,0,0,0,0]
    j=0
    dst_win = 0
    for i in dq:
        j+=1
        #d[0]=d[1]=d[2]=d[3]=d[4]=0
        if  s[0]=="O":
            t=i[0]
            d[t]+=1
        if  s[1]=="O":
            t=i[1]
            d[t]+=1
        if  s[2]=="O":
            t=i[2]
            d[t]+=1
        if  s[3]=="O":
            t=i[3]
            d[t]+=1
        if  s[4]=="O":
            t=i[4]
            d[t]+=1
        if  s[5]=="O":
            t=i[5]
            d[t]+=1
        if  s[6]=="O":
            t=i[6]
            d[t]+=1
        if  s[7]=="O":
            t=i[7]
            d[t]+=1
        if  s[8]=="O":
            t=i[8]
            d[t]+=1
        if  s[9]=="O":
            t=i[9]
            d[t]+=1
        if  s[10]=="O":
            t=i[10]
            d[t]+=1
        if  s[11]=="O":
            t=i[11]
            d[t]+=1
        if  s[12]=="O":
            t=i[12]
            d[t]+=1
        if  s[13]=="O":
            t=i[13]
            d[t]+=1
        if  s[14]=="O":
            t=i[14]
            d[t]+=1
        if  s[15]=="O":
            t=i[15]
            d[t]+=1
        if  s[16]=="O":
            t=i[16]
            d[t]+=1
        if  s[17]=="O":
            t=i[17]
            d[t]+=1
        if  s[18]=="O":
            t=i[18]
            d[t]+=1
        if  s[19]=="O":
            t=i[19]
            d[t]+=1
        if  s[20]=="O":
            t=i[20]
            d[t]+=1
        if  s[21]=="O":
            t=i[21]
            d[t]+=1
        if  s[22]=="O":
            t=i[22]
            d[t]+=1
        if  s[23]=="O":
            t=i[23]
            d[t]+=1
        if  s[24]=="O":
            t=i[24]
            d[t]+=1
        
        if  d[0] > 2:    # did we win this district?
            dst_win += 1 # add 1 to the total no. of districts won
        if  d[1] > 2:
            dst_win += 1
        if  d[2] > 2:
            dst_win += 1
        if  d[3] > 2:
            dst_win += 1
        if  d[4] > 2:
            dst_win += 1
            
        if  dst_win == 3: # Did we win 3 districts? If so we've won the election through successful Gerrymandering!
            for k in i:
                k+=1
                final_list.append(k)
                print(k,end='') #use end='' to print all k's on the same line
                
            print("final_list:",final_list)
            print("\nGood man, Gerry (solution found)!")
            print("solution found on iteration:",j,"/",len(dq))
            return_string = "".join(map(str, final_list)) # why is join command so obtuse?! Stole this off stackexchange, map function needed too apparently. Ridiculous.
            break
            
        d[0]=d[1]=d[2]=d[3]=d[4]=0
        dst_win = 0
        
    if  dst_win < 3:
        return None
        
    print("Votes/District breakdown 0-4:",d)
    
    return return_string[0:5]   + "\n"  + \
           return_string[5:10]  + "\n"  + \
           return_string[10:15] + "\n" + \
           return_string[15:20] + "\n" + \
           return_string[20:25]
