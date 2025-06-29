"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Count X’s and O’s
    x = sum(row.count(X) for row in board)
    o = sum(row.count(O) for row in board)

    # X moves first and whenever X’s count is not greater than O’s 
    return X if x<=o else O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        return set()
    possible_actions = set()
    #loop through all cells and if it's a empty cells return a tuple (i, j) of its location
    for row_index, row in enumerate(board):
        for cell_index, cell in enumerate(row):
            if cell is EMPTY:
                possible_actions.add((row_index, cell_index))
    return possible_actions            


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Before modifying anything, check that the target cell is empty.If the action is not valid (i.e., the cell already has an X or O) raise an exception 
    if action not in actions(board):
        raise Exception("Invalid action")
    
    row, col = action
    #make a deep copy of the board; we need the original board to remain unchanged. 
    copy_board = [r.copy() for r in board]

   # Find out which player's turn it is using the player(board) function.
    current_player = player(board)

    # Add X or O (depending on whose turn it is) to the action location on the copied board, and return the new board.
    #(to look at the target location at borad use row and col numbers)
    copy_board[row][col] =current_player
    return copy_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
