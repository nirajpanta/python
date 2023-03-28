# Tic Tac Toe game in Python

board = [' ' for x in range(9)]

def print_board():
    print('   |   |')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('   |   |')

def player_move(icon):
    if icon == 'X':
        number = 1
    elif icon == 'O':
        number = 2
    print('Your turn player ' + str(number))
    choice = int(input('Enter your move (1-9): ').strip())
    if board[choice - 1] == ' ':
        board[choice - 1] = icon
    else:
        print('That space is already taken!')

def is_victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

def is_draw():
    if ' ' not in board:
        return True
    else:
        return False

while True:
    print_board()
    player_move('X')
    if is_victory('X'):
        print_board()
        print('Congratulations! X wins!')
        break
    elif is_draw():
        print_board()
        print('It is a draw!')
        break
    player_move('O')
    if is_victory('O'):
        print_board()
        print('Congratulations! O wins!')
        break
    elif is_draw():
        print_board()
        print('It is a draw!')
        break