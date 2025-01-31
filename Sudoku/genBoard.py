import os
from random import sample

# Get the absolute path of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
board_path = os.path.join(script_dir, "boards", "boards.txt")
sol_path = os.path.join(script_dir, "boards", "solutions.txt")

# Ensure the 'boards' directory exists
os.makedirs(os.path.dirname(board_path), exist_ok=True)
os.makedirs(os.path.dirname(sol_path), exist_ok=True)

# To allow the board to be converted to a string for the file.txts
def array_2d_to_string(arr_2d):
    rows = [' '.join(map(str, row)) for row in arr_2d]
    return '\n'.join(rows)

base = 3
side = base * base

# pattern for a baseline valid solution
def pattern(r, c): 
    return (base * (r % base) + r // base + c) % side

# Randomize rows, columns, and numbers (of valid base pattern)
def shuffle(s): 
    return sample(s, len(s))

# Generate and write 1000 Sudoku boards
for _ in range(1000):
    rBase = range(base)
    rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
    nums = shuffle(range(1, base * base + 1))

    # Produce board using randomized baseline pattern
    board = [[nums[pattern(r, c)] for c in cols] for r in rows]

    # Write the complete board (solution) to solutions.txt
    with open(sol_path, "a") as f_sol:
        f_sol.write(array_2d_to_string(board) + "\n\n")  # Separate each board with a newline

    # Remove 75% of numbers from the board (create a puzzle)
    squares = side * side
    empties = squares * 3 // 4
    for p in sample(range(squares), empties):
        board[p // side][p % side] = 0

    # Write the puzzle board to boards.txt
    with open(board_path, "a") as f_board:
        f_board.write(array_2d_to_string(board) + "\n\n")  # Separate each board with a newline

print("1000 Sudoku boards generated and saved!")
