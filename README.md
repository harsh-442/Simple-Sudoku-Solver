# Simple-Sudoku-Solver

This is a Simple 9x9 Sudoku solver using back tracking</br></br>
Returns whether a solution exists or not, if exists, returns the solution</br>
Input is a list of lists, where each inner list is a row of the puzzle

## Functions

1.The '\_\_main\_\_' function 
  * Accepts the input puzzle and calls the solve_sudoku(puzzle) function to find the solution</br>
  * It then shows whether the puzzle is solvable or not and prints the solution or the puzzle accordingly</br></br></br>

2.The 'solve_sudoku(puzzle)' function 
  * Takes a number 1-9 as its guess and checks if the guess is valid using a helper function is_valid(puzzle,guess,row,column)</br>
  * It then calls itself recursively to fill out every blank spaces of the puzzle</br>
  * If not valid at any point of time, we backtrack and try with a new guess number
  * If neither of the guesses are valid we return False as the puzzle is UNSOLVABLE</br></br></br>
  
3.The 'is_valid(puzzle,guess,row,column)' function 
  * Checks if the guessed number is already present either in the same row, or in the same column, or in the 3x3 square it belongs to
  * If already present, it returns False</br></br></br>

4.The 'find_next_empty(puzzle)' function used in solve_sudoku function
  * Returns the next row,column on the puzzle that is not filled yet
  * Returns (None,None) if there is none
