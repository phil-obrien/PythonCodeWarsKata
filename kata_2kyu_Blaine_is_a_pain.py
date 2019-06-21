from collections import deque

#***************************
# Solution summary:
# - Create a deque representing the coords (row,col) of the route the train track takes (piece by piece). Each element in the deque is a tuple. One route-deque for each train.
# - As the train moves around the track, ROTATE the deques so the first element in the deque is the coords of the ENGINE of the train
# - There will be another, smaller deque for each train. Each represents ONLY the current coords of each engine and its carriages
# - Collisions between trains OR a train hitting itself are detected by checking if any tuple in either deque is repeated (as this means two engines/carriages are in the same spot on the route)
#***************************

def find_next_position(row, col, compass_direction, map_list):
    if  compass_direction == "N": # from here N is valid
        if  map_list[row-1][col] in ["|", "+", "/", "\\", "S"]: # valid track pieces north of here (double-backslash needed as single-backslash is an escape sequence marker!)
            #print("valid track piece north of here!")
            row -=1
            if  map_list[row][col] == "/": compass_direction = "NE"
            if  map_list[row][col] == "\\": compass_direction = "NW"
            if  map_list[row][col] in ["|", "+", "S"]: compass_direction = "N"
        else:
            print("***************** WARNING - TRACK ERROR - DERAILMENT INEVITABLE!! *****************")
        return row, col, compass_direction, map_list[row][col] == "S"


    elif compass_direction == "E": # from here E is valid
        if  map_list[row][col+1] in ["-", "+", "/", "\\", "S"]: # valid track pieces east of here
            #print("valid track piece east of here!")
            col +=1
            if  map_list[row][col] == "/": compass_direction = "NE"
            if  map_list[row][col] == "\\": compass_direction = "SE"
            if  map_list[row][col] in ["-", "+", "S"]: compass_direction = "E"
        else:
            print("***************** WARNING - TRACK ERROR - DERAILMENT INEVITABLE!! *****************")
        return row, col, compass_direction, map_list[row][col] == "S"


    elif compass_direction == "W": # from here W is valid
        if  map_list[row][col-1] in ["-", "+", "/", "\\", "S"]: # valid track pieces west of here
            #print("valid track piece west of here!")
            col -=1
            if  map_list[row][col] == "/": compass_direction = "SW"
            if  map_list[row][col] == "\\": compass_direction = "NW"
            if  map_list[row][col] in ["-", "+", "S"]: compass_direction = "W"
        else:
            print("***************** WARNING - TRACK ERROR - DERAILMENT INEVITABLE!! *****************")
        return row, col, compass_direction, map_list[row][col] == "S"


    elif compass_direction == "S": # from here S is valid
        if  map_list[row+1][col] in ["|", "+", "/", "\\", "S"]: # valid track pieces south of here
            #print("valid track piece south of here!")
            row +=1
            if  map_list[row][col] == "/": compass_direction = "SW"
            if  map_list[row][col] == "\\": compass_direction = "SE"
            if  map_list[row][col] in ["|", "+", "S"]: compass_direction = "S"
        else:
            print("***************** WARNING - TRACK ERROR - DERAILMENT INEVITABLE!! *****************")
        return row, col, compass_direction, map_list[row][col] == "S"


    elif compass_direction == "NE": # from here N, NE, E are valid
        if  map_list[row-1][col] in ["|", "+"]: # valid track pieces north of here
            #print("valid track piece north of here")
            compass_direction = "N"
            row -=1
        elif map_list[row-1][col+1] in ["/", "X", "S"]: # valid track pieces north-east of here
            #print("valid track piece north-east of here!")
            compass_direction = "NE"
            row -=1
            col +=1
        elif  map_list[row][col+1] in ["-", "+"]: # valid track pieces east of here
            #print("valid track piece east of here!")
            compass_direction = "E"
            col +=1
        else:
            print("***************** WARNING - TRACK ERROR - DERAILMENT INEVITABLE!! *****************")
        return row, col, compass_direction, map_list[row][col] == "S"


    elif compass_direction == "SE": # from here E, SE, S are valid
        if  map_list[row][col+1] in ["-", "+"]: # valid track pieces east of here
            #print("valid track piece east of here")
            compass_direction = "E"
            col +=1
        elif map_list[row+1][col+1] in ["\\", "X", "S"]: # valid track pieces south-east of here
            #print("valid track piece south-east of here!")
            compass_direction = "SE"
            row +=1
            col +=1
        elif  map_list[row+1][col] in ["|", "+"]: # valid track pieces south of here
            #print("valid track piece south of here!")
            compass_direction = "S"
            row +=1
        else:
            print("***************** WARNING - TRACK ERROR - DERAILMENT INEVITABLE!! *****************")
        return row, col, compass_direction, map_list[row][col] == "S"


    elif compass_direction == "SW": # from here S, SW, W are valid:
        if  map_list[row+1][col] in ["|", "+"]: # valid track pieces south of here
            #print("valid track piece south of here!")
            compass_direction = "S"
            row +=1
        elif map_list[row+1][col-1] in ["/", "X", "S"]: # valid track pieces south-west of here
            #print("valid track piece south-west of here!")
            compass_direction = "SW"
            row +=1
            col -=1
        elif  map_list[row][col-1] in ["-", "+"]: # valid track pieces west of here
            #print("valid track piece west of here!")
            compass_direction = "W"
            col -=1
        else:
            print("***************** WARNING - TRACK ERROR - DERAILMENT INEVITABLE!! *****************")
        return row, col, compass_direction, map_list[row][col] == "S"

                    
    elif compass_direction == "NW": # from here W, NW, N are valid:
        if map_list[row][col-1] in ["-", "+"]: # valid track pieces west of here
            #print("valid track piece west of here!")
            compass_direction = "W"
            col -=1
        elif map_list[row-1][col-1] in ["\\", "X", "S"]: # valid track pieces north-west of here
            #print("valid track piece north-west of here!")
            compass_direction = "NW"
            row -=1
            col -=1
        elif map_list[row-1][col] in ["|", "+"]: # valid track pieces north of here
            #print("valid track piece north of here!")
            compass_direction = "N"
            row -=1
        else:
            print("***************** WARNING - TRACK ERROR - DERAILMENT INEVITABLE!! *****************")
        return row, col, compass_direction, map_list[row][col] == "S"        
#*******************************************************

# 

def train_crash(track, a_train, a_train_pos, b_train, b_train_pos, limit):

    #print("a_train",a_train)
    #print("a_train_pos",a_train_pos)
    #print("b_train",b_train)
    #print("b_train_pos",b_train_pos)
    #print("limit",limit)
    map_list = track.split("\n")
    
    #print("last line",map_list[len(map_list)-1])
    if  map_list[len(map_list)-1].strip() == "": # the occasional map has a blank last line so remove it
        map_list.pop()
    
    max_string_len = 0
    for i in map_list:
        max_string_len = max(max_string_len,len(i.rstrip())) # find out which string is the longest - this will be our map width
                                                             # Note that the rstrip() function is needed as some lines of the map have trailing spaces which we
                                                             # do not want to count
    
    for i in range(0, len(map_list)):
        map_list[i] = "*" + map_list[i].rstrip() + (" " * (max_string_len - len(map_list[i].rstrip() ))) + "*"    # place an asterisk at the start and end of each line in the map
    
    map_list.insert(0, ("*" * (max_string_len + 2)))    # add a line of ***'s to the top and bottom of the map. The map is now trimmed of all unnecessary spaces and surrounded
    map_list.append("*" * (max_string_len + 2))         # by a border of ***'s. This border makes the route-finder function "find_next_position" simpler as there is no need to
                                                        # to test for index out of bounds when trying to find the next valid piece of track

    #print("map:")
    #for i in map_list:
    #    print(i)

    row = 1
    col = map_list[row].index("/")  # "Position Zero" is always the first non-blank char on top line (row 1 once border of ***'s is added)
                                    # The track shape in this position will ALWAYS be "/" because we know the track is a circuit, and
                                    # that circuit must re-join the top line with a "/" track piece! Simple, and handy!
                                    # idx is the column in which "Position Zero" is found.
    
    dq_a_train_coords = deque([])   # Both trains have identical routes as they follow the same track. They have the potential to follow the route in a different manner,
    dq_b_train_coords = deque([])   # e.g. different start points, express trains (Xxxx) don't stop at stations, any train can travel either clockwise or anti-clockwise

    a_train_length = len(a_train)
    b_train_length = len(b_train)

    set_of_stations = set()

    zero_position_coords = (row,col) # create a tuple with row,col as elements
    compass_direction = "E"

    track_complete = False

    current_coords = tuple(zero_position_coords)

    dq_a_train_coords.append(zero_position_coords)  # The deque for each train route is made up of tuples of coordinates. Each tuple contains a "row" and "column" coord,
    dq_b_train_coords.append(zero_position_coords)  # so the tuples represent the track-route on a track-piece by track-piece basis. Each deque begins at "Position Zero"

    while not track_complete:
        row, col, compass_direction, at_station = find_next_position(row, col, compass_direction, map_list) # feed in current position, direction and the map, and this function will
                                                                                                            # return the coords, direction and boolean at_station of the next track piece
        if  (row,col) == zero_position_coords: # if we find ourselves back at Position Zero, route is mapped!
            track_complete = True
            continue    # "contine" command will bring us immediately back to the while loop which we will then immediately exit

        tupled_coords = (row,col)               # Create a tuple out of row and col returned from the find_next_position function
        dq_a_train_coords.append(tupled_coords) # Add that new tuple to each deque
        dq_b_train_coords.append(tupled_coords)

        if  at_station:                     # Add the coords as a tuple as we cannot add lists to sets because lists are mutable!
            set_of_stations.add((row,col))  # Double-parenthesis "(())" required here to designate (row,col) as a single element (a tuple) 
                                            # rather than row,col (two integers)


    #print("set_of_stations",set_of_stations)
    #print("A deque",dq_a_train_coords)

    # We now have 2 deques, one for the route of Train A, one for the route of Train B. They're identical for now.
    # Although their contents won't change, the order of the content will as deques are rotated to reflect train position


    # Depending on whether we're going clockwise or anti-clockwise, we set up a_train_direction variable. Train direction is determined by where the Engine is
    # in relation to the carriages. Engine is designated by upper case letter, carriages by lower case. Engine will always be in either first or last position.
    if  a_train[0].upper() == a_train[0]: # e.g. Aaaaa, train is going anti-clockwise from Point Zero,
        a_train_direction = 1             # we'll rotate backwards through deque (i.e. deque 1,2,3,4 becomes 4,1,2,3 when rotated by 1)
    else:                                 # Else we must have e.g. aaaaA, i.e. train is going clockwise from Point Zero
        a_train_direction = -1            # we'll rotate forwards through deque (i.e. deque 1,2,3,4 becomes 2,3,4,1 when rotated by -1)

    # Bring Train A to its starting point. Train position is always clockwise from Point Zero, irrespective of whether train direction is clockwise or anti-clockwise:
    if  a_train_pos != 0:
        dq_a_train_coords.rotate(a_train_pos * -1) # rotate deque as far as needed (a_train_pos => rotate this many times, -1 => clockwise)

    # Set up Train B direction as per Train A above:
    if  b_train[0].upper() == b_train[0]:
        b_train_direction = 1
    else:
        b_train_direction = -1

    # Bring Train B to its starting point:
    if  b_train_pos != 0:
        dq_b_train_coords.rotate(b_train_pos * -1)


    # We now want to populate two more deques, each representing ONLY the current coords of Train A and Train B engines and carriages:
    dq_a_train_and_carriages = deque([], maxlen = a_train_length) # the maxlen property ensures that as we add elements to one end of the deque, they are removed from the other end if maxlen exceeded
    for i in range(0, a_train_length):
        dq_a_train_and_carriages.append(dq_a_train_coords[i * a_train_direction])

    dq_b_train_and_carriages = deque([], maxlen = b_train_length)
    for i in range(0, b_train_length):
        dq_b_train_and_carriages.append(dq_b_train_coords[i * b_train_direction])

    #print("A-Train+Cars",dq_a_train_and_carriages)
    #print("B-Train+Cars",dq_b_train_and_carriages)

    #print ("initial_coords A:",dq_a_train_coords[0])
    #print ("initial_coords B:",dq_b_train_coords[0])

# Next up we move the trains one step at a time for up to "limit" number of steps.
# Also, build in a loop-delay whenever a non express train reaches a station.
# Create a set for each train (& carriages) after each move and test INTERSECT of sets
# If any common elements => TRAIN CRASH!!!

    a_train_station_delay = 0
    b_train_station_delay = 0

    for time_step in range(0, limit+1):
        #print("T=", time_step, "Engine A=", dq_a_train_coords[0], "Engine B=", dq_b_train_coords[0])
        #print("Full A:", dq_a_train_and_carriages)
        #print("Full B:", dq_b_train_and_carriages)

        # ****** COLLISION DETECTIONS *************
        # Between the two trains:
        for i in dq_a_train_and_carriages:      # If the engine or any carriage of a_train shares the coords with
            if  i in dq_b_train_and_carriages:  # the engine or any carriage of b_train, COLLISION!
                print("return",time_step)
                return time_step                # Return "when" the collision happened
                
        # One train hitting itself is also possible (remember "Snake" game!) - convert deque A to set. If set is shorter => duplicate coords in deque => COLLISION! 
        test_collision_set = set(dq_a_train_and_carriages)
        if  len(test_collision_set) != len(dq_a_train_and_carriages):
            print("return (self-collision A)",time_step)
            return time_step                # Return "when" the collision happened

        # One train hitting itself is also possible (remember "Snake" game!) - convert deque B to set. If set is shorter => duplicate coords in deque => COLLISION!
        test_collision_set = set(dq_b_train_and_carriages)
        if  len(test_collision_set) != len(dq_b_train_and_carriages):
            print("return (self-collision B)",time_step)
            return time_step                # Return "when" the collision happened

    # move the trains along unless the relevant train_station_delay is > 0
        if  a_train_station_delay > 0:
            a_train_station_delay -= 1
            if  a_train_station_delay == 0:
                dq_a_train_coords.rotate(a_train_direction)
                dq_a_train_and_carriages.appendleft(dq_a_train_coords[0]) # the new coord replaces where train was and all other coords move back 1 (the last coord "falls off")
        else:
            dq_a_train_coords.rotate(a_train_direction)
            dq_a_train_and_carriages.appendleft(dq_a_train_coords[0]) # the new coord replaces where train was and all other coords move back 1 (the last coord "falls off")
            
        if  b_train_station_delay > 0:
            b_train_station_delay -= 1
            if  b_train_station_delay == 0:
                dq_b_train_coords.rotate(b_train_direction)
                dq_b_train_and_carriages.appendleft(dq_b_train_coords[0]) # the new coord replaces where train was and all other coords move back 1 (the last coord "falls off")
        else:
            dq_b_train_coords.rotate(b_train_direction)
            dq_b_train_and_carriages.appendleft(dq_b_train_coords[0]) # the new coord replaces where train was and all other coords move back 1 (the last coord "falls off")

# if train is at a station, set delay before departure unless train is Express (X) or timer already underway
        if  dq_a_train_coords[0] in set_of_stations \
        and a_train[0].upper() != "X"                 \
        and a_train_station_delay == 0:
            a_train_station_delay = a_train_length

# if train is at a station, set delay before departure unless train is Express (X) or timer already underway
        if  dq_b_train_coords[0] in set_of_stations \
        and b_train[0].upper() != "X"                 \
        and b_train_station_delay == 0:
            b_train_station_delay = b_train_length

    print("return -1")
    return -1
