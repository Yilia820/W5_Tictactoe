from W5_logic import make_empty_board, get_winner, other_player
def print_board(board):
    for i in range(3):
        print(board[i])

def player_input(board,player,position):
    board[position[0]][position[1]]= player
    return board

board = make_empty_board()
winner = 'None'
Player = "O"
while winner == 'None':
    print('TODO: take a turn!')
    #TODO: Show the board to the user.
    #TODO: Input a move from the player.
    #TODO: Update the board.
    #TODO: Update who's turn it is.
    print_board(board)
    position = input("enter position, ex(0,0),(0,1): ")
    board= player_input(board, Player,position)
    Player = other_player(Player)
    winner = get_winner(board)
print_board(board)
print(winner, "  is winner")