EMPTY = None
board =[["a", "b", "c"],
        [1, EMPTY, 3],
        ["x", "y", "z"]]


moves = set()
for row in range(3):          # row will be 0, 1, 2
    for col in range(3):      # col will be 0, 1, 2
        if board[row][col] == EMPTY:
            # You now have both the indices and the cell value
            moves.add((row, col))