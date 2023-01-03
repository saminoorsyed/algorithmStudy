# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# Approach:
# here we will perform a nested binary search, the first layer will search compare the target to the first number in each row
# if the number is greater than row1 and less than row2, then we should search row1 using binary search

def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    """
    to perform a binary search on a sorted list, we can use a while loop
    """
    rows, cols = len(matrix), len(matrix[0])
    low, hi = 0, rows*cols-1

    while low<=hi:
        middle = (low+hi)//2
        number= matrix[middle//cols][middle%cols]
        if number == target:
            return True
        if number>target:
            hi = middle-1
        else:
            low = middle+1
    return False




if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    print(searchMatrix(matrix, target))
# Output: true
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13
    print(searchMatrix(matrix, target))
# Output: false
    matrix = [[1,1]]
    target = 2
    print(searchMatrix(matrix, target))
# Output: false
    matrix = [[1,3]]
    target = 1
    print(searchMatrix(matrix, target))
# Output: false