def create_list_of_ships(ship, param_horzntal_battleField, param_vertical_battleField):

    list_of_ships = []

  # Horizontal check first:
    for line in range(0,10):
        if ship in param_horzntal_battleField[line]:
            offset = 0
            start_offset = 0  # we will start our search at this index (covers case where > 1 ship on same line)
            while offset > -1:
                offset = param_horzntal_battleField[line].find(ship,start_offset)
                if offset == -1:  # no (or no more) ships on this line of the battlefield
                    continue      # skip on to the next iteration of the WHILE loop (from which we will immediately exit due to -1)
                ship_orientation = 'h'
                start_offset = offset + 1 # start next search at one point after where we found a ship
                list_of_ships.append([line, offset, ship_orientation])

  # Vertical check next:
    for line in range(0,10):
        if ship in param_vertical_battleField[line]:
            offset = 0
            start_offset = 0  # we will start our search at this index (covers case where > 1 ship on same line)
            while offset > -1:
                offset = param_vertical_battleField[line].find(ship,start_offset)
                if offset == -1:  # no (or no more) ships on this line of the battlefield
                    continue      # skip on to the next iteration of the WHILE loop (from which we will immediately exit due to -1)
                ship_orientation = 'v'
                start_offset = offset + 1 # start next search at one point after where we found a ship
                list_of_ships.append([line, offset, ship_orientation])

    return list_of_ships

def update_horzntal_battleField(ship_coords, ship_string, param_horzntal_battleField):
    line             = ship_coords[0]
    offset           = ship_coords[1]
    ship_orientation = ship_coords[2]
    ship_char        = ship_string[0] # grab any char from ship_string (eg 3 from 333)
    
    if  ship_orientation == 'h':
        temp_line = param_horzntal_battleField[line]
        temp_line = temp_line[0:offset] + ship_string + temp_line[(offset+len(ship_string)):]
        param_horzntal_battleField[line] = temp_line
    else:  # ship_orientation must be 'v' if it's not 'h'
        for i in range(0,len(ship_string)):    # when dealing with vertical ship: line is offset and offset is line
            param_horzntal_battleField[offset+i] = param_horzntal_battleField[offset+i][:line] + ship_char + param_horzntal_battleField[offset+i][line+1:]

    return param_horzntal_battleField
    
def update_vertical_battleField(ship_coords, ship_string, param_vertical_battleField):
    line             = ship_coords[0]
    offset           = ship_coords[1]
    ship_orientation = ship_coords[2]
    ship_char        = ship_string[0] # grab any char from ship_string (eg 3 from 333)

    if  ship_orientation == 'v':
        temp_line = param_vertical_battleField[line]
        temp_line = temp_line[0:offset] + ship_string + temp_line[(offset+len(ship_string)):]
        param_vertical_battleField[line] = temp_line
    else:  # ship_orientation must be 'h' if it's not 'v'
        for i in range(0,len(ship_string)):    # when dealing with horizontal ship: line is offset and offset is line
            param_vertical_battleField[offset+i] = param_vertical_battleField[offset+i][:line] + ship_char + param_vertical_battleField[offset+i][line+1:]

    return param_vertical_battleField

######################################
####### MAIN FUNCTION: ###############
######################################
def validate_battlefield(battleField):
    
# make sure we have the right number of ones (20 in total)
    total_ones = 0
    
    for i in battleField:
        total_ones += i.count(1)
        
    if  total_ones != 20:
        return False

# The map we have is a list of 10 horizontal lists.
# Let's convert that into two lists of strings, one 
# a horizontal version (similar layout to original)
# and one vertical version e.g.:
# This list of lists:
#[[0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
# [0, 0, 1, 0, 0, 0, 0, 0, 1, 1],
# [0, 0, 1, 0, 1, 1, 1, 0, 1, 1],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
# [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
# [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
#
# ...becomes these Lists of Strings:
# Horizontal String Map:
#  0000011001
#  0010000011
#  0010111011
#  0000000001
#  0000000000
#  0000111000
#  0000000010
#  0001000000
#  0000000100
#  1000000000
# Vertical String Map:
#  0000000001
#  0000000000
#  0110000000
#  0000000100
#  0010010000
#  1010010000
#  1010010000
#  0000000010
#  0110001000
#  1111000000
#
# ...this makes the ships easier to search for irrespective of orientation
# (i.e. ship is horizontal or vertical on original List of Lists)
# because we can search for substrings in strings (in both directions h & v)
#

    horzntal_battleField = ['','','','','','','','','','']
    vertical_battleField = ['','','','','','','','','','']

    for col in range(0,10):
        for row in range(0,10):
            c = str(battleField[row][col])
            horzntal_battleField[row] += c
            vertical_battleField[col] += c    

# The following algorithm works by:
# Finding all possibilities of where the battleship (1111) can be (and storing their details in a list)
#  - For each potential battleship, find all possibilities of a first cruiser (111)
#    - For each potential first cruiser, find all possibilities of a second cruiser (111)
#     - For each potential second cruiser, find all possibilities of first destroyer (11)
#       - For each potential first destroyer, find all possibilities of second destroyer (11)
#         -  For each potential second destroyer, find all possibilities of third destroyer (11)
#         -  As soon as we have found a single valid THIRD destroyer, we KNOW the battlefield is valid
#            because the only remaining ships are submarines (1) and we've already verified there are 20 1's

    list_of_battleships = create_list_of_ships('1111', horzntal_battleField, vertical_battleField)

    for battleship in list_of_battleships:
        temp_1_horzntal_battleField = list(horzntal_battleField) # we'll update these temp maps
        temp_1_vertical_battleField = list(vertical_battleField) # as we find valid ships below

        temp_1_horzntal_battleField = update_horzntal_battleField(battleship,'4444',temp_1_horzntal_battleField)
        temp_1_vertical_battleField = update_vertical_battleField(battleship,'4444',temp_1_vertical_battleField)

        list_of_first_cruisers = create_list_of_ships('111', temp_1_horzntal_battleField, temp_1_vertical_battleField)
        #print("list_of_first_cruisers",list_of_first_cruisers)

        for first_cruiser in list_of_first_cruisers:
            temp_2_horzntal_battleField = list(temp_1_horzntal_battleField) # temp2 has battleship &
            temp_2_vertical_battleField = list(temp_1_vertical_battleField) # we'll add first cruiser

            temp_2_horzntal_battleField = update_horzntal_battleField(first_cruiser,'333',temp_2_horzntal_battleField)
            temp_2_vertical_battleField = update_vertical_battleField(first_cruiser,'333',temp_2_vertical_battleField)

            list_of_second_cruisers = create_list_of_ships('111', temp_2_horzntal_battleField, temp_2_vertical_battleField)

            for second_cruiser in list_of_second_cruisers:
                temp_3_horzntal_battleField = list(temp_2_horzntal_battleField) # temp3 has battleship & 1st cruiser
                temp_3_vertical_battleField = list(temp_2_vertical_battleField) # we'll add 2nd cruiser

                temp_3_horzntal_battleField = update_horzntal_battleField(second_cruiser,'333',temp_3_horzntal_battleField)
                temp_3_vertical_battleField = update_vertical_battleField(second_cruiser,'333',temp_3_vertical_battleField)

                list_of_first_destroyers = create_list_of_ships('11', temp_3_horzntal_battleField, temp_3_vertical_battleField)

                for first_destroyer in list_of_first_destroyers:
                    temp_4_horzntal_battleField = list(temp_3_horzntal_battleField) # temp4 has battleship, both cruisers
                    temp_4_vertical_battleField = list(temp_3_vertical_battleField) # we'll add first destroyer

                    temp_4_horzntal_battleField = update_horzntal_battleField(first_destroyer,'22',temp_4_horzntal_battleField)
                    temp_4_vertical_battleField = update_vertical_battleField(first_destroyer,'22',temp_4_vertical_battleField)
                
                    list_of_second_destroyers = create_list_of_ships('11', temp_4_horzntal_battleField, temp_4_vertical_battleField)
                    
                    for second_destroyer in list_of_second_destroyers:
                        temp_5_horzntal_battleField = list(temp_4_horzntal_battleField) # temp5 has battleship, both cruisers, first destroyer
                        temp_5_vertical_battleField = list(temp_4_vertical_battleField) # we'll add second destroyer

                        temp_5_horzntal_battleField = update_horzntal_battleField(second_destroyer,'22',temp_5_horzntal_battleField)
                        temp_5_vertical_battleField = update_vertical_battleField(second_destroyer,'22',temp_5_vertical_battleField)
                    
                        list_of_third_destroyers = create_list_of_ships('11', temp_5_horzntal_battleField, temp_5_vertical_battleField)
                        
                        if  len(list_of_third_destroyers) > 0:
                            return True  # if we get to this point it means we've found a valid spot for all ships except submarines...but they're always valid!

    return False # if we get to this point, we've exhausted all permutations of the battleField and can't find a way to validly fit all ships

#####################
#Interesting solution by daddepledge, user9993130, jdifjdf

def validateBattlefield_2(field):
    return battle(set([(r, c) for c in range(10) for r in range(10) if field[r][c]]), [1,1,1,1,2,2,2,3,3,4]) 
  
def battle(grid, fleet):
    return sum(fleet) == len(grid) and (fleet == [] or any(battle(grid - p, fleet[:-1]) for p in possibles(grid, fleet[-1])))

def possibles(grid, ship):
    return [set(p) for p in [[(r+i,c) for i in range(ship)] for r, c in grid] + [[(r,c+i) for i in range(ship)] for r,c in grid] if set(p) <= grid]

#####################
