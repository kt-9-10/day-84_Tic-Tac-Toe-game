import random
import time

TITLE = '''
▀█▀ █ █▀▀   ▀█▀ ▄▀█ █▀▀   ▀█▀ █▀█ █▀▀
░█░ █ █▄▄   ░█░ █▀█ █▄▄   ░█░ █▄█ ██▄
'''

def display_board(board):
    print('-------------')
    for row in board:
        print(f"| {' | '.join(row)} |")
        print('-------------')


def select_position(board):
    while True:
        try:
            row = int(input('Select row (0, 1, 2): '))
            column = int(input('Select column (0, 1, 2): '))
            if board[row][column] == ' ':
                board[row][column] = 'X'
                break
            else:
                print('This position is already filled.')
        except (ValueError, IndexError):
            print('This input is an invalid value.')


def check_winner(board):
    # row check
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]
    # column check
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
            return board[0][i]
    # diagonal check
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    # no winner
    return None


def check_reach(board, player):
    # row check
    for row in range(3):
        if board[row].count(player) == 2 and board[row].count(' ') == 1:
            return row, board[row].index(' ')
    # column check
    for col in range(3):
        column = [board[row][col] for row in range(3)]
        if column.count(player) == 2 and column.count(' ') == 1:
            return column.index(' '), col
    # diagonal check
    diagonal1 = [board[0][0], board[1][1], board[2][2]]
    if diagonal1.count(player) == 2 and diagonal1.count(' ') == 1:
        return diagonal1.index(' '), diagonal1.index(' ')
    diagonal2 = [board[0][2], board[1][1], board[2][0]]
    if diagonal2.count(player) == 2 and diagonal2.count(' ') == 1:
        return diagonal2.index(' '), 2 - diagonal2.index(' ')
    # no reach
    return None


def select_position_by_cpu(board):
    reach_position = check_reach(board, 'O')
    if reach_position:
        board[reach_position[0]][reach_position[1]] = 'O'
        return

    reach_position = check_reach(board, 'X')
    if reach_position:
        board[reach_position[0]][reach_position[1]] = 'O'
        return

    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == ' ':
            board[row][col] = 'O'
            return


def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True


def play_game():
    print(TITLE)
    time.sleep(1)

    board = [[' ', ' ', ' '] for i in range(3)]
    while True:
        display_board(board)

        # Player's turn (X)
        print("It's your turn.")
        select_position(board)
        display_board(board)

        # Check for a winner or draw after your turn
        winner = check_winner(board)
        if winner:
            print(f"You win!")
            break

        if is_board_full(board):
            print("It's a draw!")
            break

        # Computer's turn (O)
        print("Computer's turn.")
        time.sleep(1)
        select_position_by_cpu(board)

        # Check for a winner or draw after computer's turn
        winner = check_winner(board)
        if winner:
            display_board(board)
            print(f"You lose...")
            break

        if is_board_full(board):
            print("It's a draw!")
            break


play_game()
