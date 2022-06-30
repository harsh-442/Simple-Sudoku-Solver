# sudoku solver using back tracking
# returns whether a solution exists or not
# returns the solution if it exists
#input is a list of lists, where each inner list is a row of our sudoku puzzle
#the find_next_empty function returns the next row,column on the puzzle that is not filled yet
#find_next_empty returns (None,None) if there is none

def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c]==-1:
                return r,c
    return None,None

def is_valid(puzzle,n,r,c):
    if n in puzzle[r]:          #rowwise
        return False
    cols_val=[]
    for i in range(9):
        cols_val.append(puzzle[i][c])
    if n in cols_val:           #columnwise
        return False
    row_start= (r//3)*3
    col_start=(c//3)*3
    
    for i in range(row_start,row_start+3):
        for j in range(col_start,col_start+3):
            if puzzle[i][j]==n:
                return False
    return True
    

def solve_sudoku(puzzle):
    row,column=find_next_empty(puzzle)
    
    if row is None:
        return True
    for n in range(1,10):
        if is_valid(puzzle,n,row,column):
            puzzle[row][column]=n
            
            if solve_sudoku(puzzle):        #recursion for all elements of the puzzle
                return True

        puzzle[row][column]=-1     #if not valid, backtrack and try a new number
    return False            # the puzzle is UNSOLVABLE


if __name__=='__main__':
    puzzle=[[],[],[],[],[],[],[],[],[]]   
    print("Enter puzzle, -1 if blank")
    for i in range(9):
        for j in range(9): 
            print("Enter puzzle[",i+1,",",j+1,"] : ",end=" ",sep="")
            puzzle[i].append(int(input()))
    if solve_sudoku(puzzle):
        print("Solvable\n---Solution---")
    else:
        print("Not Solvable\n---Puzzle---")
    for i in puzzle:
        print(i)
