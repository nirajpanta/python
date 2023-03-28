#Create Board
board=[
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']
]

player = ['X','O']
board_size = 3

# player_turn 

def print_board():
    print("\n      1   2   3\n")
    for i in range(board_size):
        print(f"{i+1}",end='')
        for j in range(board_size):
            print(" | "+board[i][j], end='')

        if(i!=2):
            print("\n   ---+---+---+---")
        else:
            print()

if __name__ == '_main_':
    print_board()
    print(f'Input value for player {player[0]}')
    row = int(input('Enter row: '))
    column = int(input('Enter column: '))

    board[row][column] = 'X'
    print_board()


