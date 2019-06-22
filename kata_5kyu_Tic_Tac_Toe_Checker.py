def isSolved(board):
    for i in board: # test winner across
        print i
        if  i==[1,1,1] or i==[2,2,2]:
            return i[0]
        
    for i in range(0,3): # test winner down
        for winner in range(1,3):
            if  board[0][i] == winner \
            and board[1][i] == winner \
            and board[2][i] == winner:
                return winner
                
    for winner in range(1,3): # test diagonals
        if  board[0][0] == winner \
        and board[1][1] == winner \
        and board[2][2] == winner:
            return winner
            
        if  board[0][2] == winner \
        and board[1][1] == winner \
        and board[2][0] == winner:
            return winner
            
    for i in board: # any blanks left? game unfinished
        if  0 in i:
            return -1
            
    return 0 # no spaces left and no winner? cat's game (draw!)
