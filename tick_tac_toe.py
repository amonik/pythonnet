from random import randrange


def display_board(board):
    plus_minus = ("+" + "-" * 7) * 2 + "+" + "-" * 7 + "+"
    dash = "|       |       |       |"
    dash_var = "|   %s   |   %s   |   %s   |"
    if board:
        board_output = plus_minus  \
                       + "\n" + dash + "\n" + dash_var % \
                       (board[0][0], board[0][1], board[0][2]) + \
                       "\n" + dash + "\n" + plus_minus + "\n" \
                       + dash + "\n" + dash_var % \
                       (board[1][0], board[1][1], board[1][2]) + \
                       "\n" + dash + "\n" + plus_minus + \
                       "\n" + dash + "\n" + dash_var % \
                       (board[2][0], board[2][1], board[2][2]) + \
                       "\n" + dash + "\n" + plus_minus
        return board_output
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.


def enter_move(board):
    your_move = int(input("What is your move, please select numbers 1 to 9 if available: "))
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == your_move:
                board[i][j] = "O"
    return board
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.


def make_list_of_free_fields(board):
    free_squares = []
    for i in range(len(board)):
        for j in range(len(board)):
            if type(board[i][j]) == int:
                free_squares.append((i, j,))
    return free_squares
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.


def victory_for(board, sign):
    n = 0
    for i in range(len(board)):
        if board[0][i] == sign:
            n += 1
            if n == 3:
                return "Player with {} won the game".format(sign)
            else:
                n = 0
        elif board[1][i] == sign:
            n += 1
            if n == 3:
                return "Player with {} won the game".format(sign)
            else:
                n = 0
        elif board[2][i] == sign:
            n += 1
            if n == 3:
                return "Player with {} won the game".format(sign)
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game


def draw_move(board):
    computer_move = randrange(1, 10)
    for i in range(board):
        for j in range(board):
            if board[i][j] == computer_move:
                board[i][j] = "X"
    return board

    # The function draws the computer's move and updates the board.


def main():
    # Create new board
    n = 0
    storage_board = [[i for i in range(3)] for j in range(3)]
    for i in range(len(storage_board)):
        for j in range(len(storage_board)):
            n += 1
            storage_board[i][j] = n
    storage_board[1][1] = 'X'
    print(display_board(storage_board))


if __name__ == '__main__':
    main()
