# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

# Intuition:
# There is a lot of overlap in the checks for this problem. I believe that the best way to check this solution
# would be to check each row column and square each time that an element of the board is processed rather than 
# checking a row, a column and then the squares.
# Approach:
# To check each value, I believe that having a dictionary for each row, column and square that with key values 1-9
# as each square in the boar is processed, its coordinates (x,y) will direct which dictionary to check, once a value
# is found, the value of it's key will incremented by one. if the value is already one, the sodoku is invalid.
# the checks should run in O(1) time

def isValidSudoku(board: list[list[str]]) -> bool:
        """
        create a dictionary key for each row
        create a dictionary key for each row
        create a dictionary key for each square (r//3, c//3)
        """
        rows = {}
        cols = {}
        sqs = {}
        
        # each check function operates in O(1) time since it uses a dictionary as a hash
        def check_row(x, val):
            # if the row has not yet been checked, add it to the rows dictionary
            if x not in rows:
                rows[x]={}
            # if the value has already been entered return false
            if val in rows[x]:
                return False
            # add the current value to the dictionary as a key
            rows[x][val] = 1
            return True

        def check_col(y,val):
            # if the column has not already been checked, add it to the cols dictionary
            if y not in cols:
                cols[y]={}
            # if the value is already checked, return false
            if val in cols[y]:
                return False
            cols[y][val] = 1
            return True

        def check_sqs(x,y, val):
            # determine the square to be checked
            x_square = x//3
            y_square = y//3
            # if the square has not been checked once, add it as a dictionary
            if (x_square, y_square) not in sqs:
                sqs[(x_square,y_square)]={}
            # if the value is already in the square dictionary, return False
            if val in sqs[(x_square,y_square)]:
                return False
            # add the value to the square dictionary as a key and return true
            sqs[(x_square,y_square)][val]=1
            return True
            

        # loop through each coordinare in the array and check the corresponding row, column and dictionary of each
        for y_coord, row in enumerate(board):
            for x_coord, value in enumerate(row):
                # continue if the value is not a number
                if value == ".":
                    continue
                if (check_col(y_coord, value) and check_row(x_coord, value) and check_sqs(x_coord, y_coord, value)):
                    continue            
                return False
        
        return True



if __name__ == "__main__":
    board = [
         ["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

    board1 =[
         ["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

    print(isValidSudoku(board))
    # should return true

    print(isValidSudoku(board1))
    # should return false

    