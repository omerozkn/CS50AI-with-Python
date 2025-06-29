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
    # Check if the game is over using terminal(board). If it is, return an empty set.
    if terminal(board):
        return set()
    # Create an empty set to hold all possible (row, column) actions.
    possible_actions = set()
    # Loop through all cells of the board.
    # For each cell, if it is EMPTY, add its (row_index, column_index) as a tuple to the set.
    for row_index, row in enumerate(board):
        for column_index, cell in enumerate(row):
            if cell is EMPTY:
                possible_actions.add((row_index, column_index))
    return possible_actions            


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Validate the action: raise an Exception if the cell is already occupied or the action is illegal.
    if action not in actions(board):
        raise Exception("Invalid action")
    
    row, col = action
    # Make a deep copy of the board to avoid modifying the original.
    copy_board = [r.copy() for r in board]

   # Use player(board) to determine whose turn it is (X or O).
    current_player = player(board)

    # Apply the move to the copied board at the specified row and column and Return the modified copy board
    
    copy_board[row][col] =current_player
    return copy_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    


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
