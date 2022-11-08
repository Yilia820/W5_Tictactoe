def make_empty_board():
    return[
        ['None','None','None'],
        ['None','None','None'],
        ['None','None','None'],
    ]
def get_winner(board):
    '''Determines the winner of the given board.
    Return 'x','0',or None.'''
    Flag = 0                                            # flag for Draw or someone win
    str_H = ""                                          # Horizental decision
    str_V = ""                                          # Vertical decision
    str_C1 = ""                                         # Left cross decision
    str_C2 = ""                                         # Right cross decision
    for i in range(3):
        str_H = ""
        str_V = ""
        for j in range(3):
            str_H = str_H+board[i][j]                                                  
            str_V = str_V+board[j][i]
            if i==j:
                str_C1 = str_C1+board[i][j]
            if (i==2 and j==0) or (i==1 and j==1) or (i==0 and j==2):
                str_C2 = str_C2+board[i][j]

            if str_H == "OOO" or str_V == "OOO" or str_C1 == "OOO"or str_C2 == "OOO":    #check for "O" win or not
                return "O"
                Flag = 1
                break
            if str_H == "XXX" or str_V == "XXX" or str_C1 == "XXX" or str_C2 == "XXX":   #check for "X" win or not
                return "X"
                Flag = 1
                break
    if Flag == 0:                                                                        # If no one win, print "Draw"
        return "None"

    return 'None' 

def other_player(player):
    '''Given the character for a player, returns the other player.'''
    if player == "X":
        return 'O' #FIXME
    if player == "O":
        return 'X' #FIXME

