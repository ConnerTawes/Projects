import os
from random import sample

# Get the absolute path of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
board_path = os.path.join(script_dir, "..", "boards", "boards.txt")
sol_path = os.path.join(script_dir, "boards", "solutions.txt")

# Ensure the 'boards' directory exists
os.makedirs(os.path.dirname(board_path), exist_ok=True)
os.makedirs(os.path.dirname(sol_path), exist_ok=True)

# Global array that holds all of the sudoku boards
allBoards = []

# This class holds the numebr of a space and if it was origionally there or not
class sudokuSpace:
  def __init__(self, num, valid):
    self.num = num
    self.valid = valid


# This function prints out the numbers of any given board
def printBoard(board):
  for row in board:
    for num in row:
      print(num.num, " ", end='')
    print()

# This file reads in the boards from boards.txt to the global array allBoards
def readBoardsFromFile():
  f = open(board_path, "r")
  boardString = f.read()
  # This deletes the last two new line characters
  boardString = boardString[:-2]
  # Seperate each board
  boardArray = boardString.split('\n\n')
  for board in boardArray:
    boardRows = []
    # Seperate each row
    row = board.split('\n')
    for col in row:
      # Seperate each column to convert all of the numbers from strings to ints
      intOfNums = []
      nums = col.split(' ')
      for num in nums:
        # We store the numbers in this object which hold the numebr value along with if the
        # number was provided or not
        numInSpace = sudokuSpace(int(num), int(num) == 0)
        intOfNums.append(numInSpace)

      # Append the int array of the numbers in a row to rows. This will be used to rebuild
      # the boards but as int instead of string
      boardRows.append(intOfNums)
    # This appends after all of the rows in a board have been converted to an int so we then
    # append it to allBoards as it is the full board converted
    allBoards.append(boardRows)


# This function checks to make sure the number is not already in either the row or the column
def checkIfSafe(board, rowLoc, colLoc, num):
  # Check if the column is safe
  for rowNum in range(len(board)):
    if board[rowNum][colLoc].num == num:
      return False
  # Check if the row is safe
  for colNum in range(len(board[0])):
    if board[rowLoc][colNum].num == num:
      return False 
  # If it made it out of those loops, it is valid
  return True


# This function will continually try numbers going left to right top to bottom trying numbers
# from 1 through 9 till a solution is found.
def solveBoard(board):
  # Iterate through the board
  for row in range(len(board)):
    for col in range(len(board[0])):
      # See if the number is changable
      if board[row][col].valid == True:
        numFound = False

        # Makes it so that the starting number is a number 1-9
        startingTestNum = 0
        if board[row][col].num == 0: 
          startingTestNum = 1
        else:
          startingTestNum = board[row][col].num
          
        # Checks from the number on the board to 9
        for testNum in range(startingTestNum, 10):
          if checkIfSafe(board, row, col, testNum):
            board[row][col] = sudokuSpace(testNum, True)
            numFound = True
            break
          
        # If a number did not work, make this number 0, go to the previous space and iterate
        # it to the next valid number
        if not numFound:
          board[row][col] = sudokuSpace(0, True)

          # If testing on column 0, set the column to 7 (so it can iterate to the last column
          # after after this flow), set the row to the previous row.
          # 
          # o o o o     ->     o o o x
          # x o o o            o o o o
          # 
          # If it is not on the first column, then go back to the previous column to continue
          # iterating that number. (The minus 2 allows the flow to iterate to the next column
          # and then it is in the correct space)
          # o o o o     ->     o o o o
          # o o x o            o x o o
          if col == 0 and row != 0:
            col = 7
            row = row - 1 
          else:
            col = col - 2
   
  printBoard(board)

readBoardsFromFile()
solveBoard(allBoards[0])

print("Finished")