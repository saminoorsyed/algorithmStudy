"""Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3"""

def num_islands(grid: list[list[str]])-> int:
    land = dict()
    stack = []
    islands = 0
    #loop through each piece of land
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # check if the piece of land is in the dictionary 
            if (row, col) not in land and grid[row][col] == "1":
                # add 1 for each new island
                islands += 1
                stack.append((row, col))
                while stack:
                    # add land to dictionary
                    curr_land = stack.pop()
                    r = curr_land[0]
                    c = curr_land[1]
                    # if the coordinates are out of bounds
                    if 0 >r or r >= len(grid) or 0>c or c >= len(grid[0]):
                        continue
                    land[curr_land] = grid[r][c]
                    # move to the next stack item if value is 0
                    if land[curr_land] == "0":
                        continue
                    #have to check in all directions, add if not already checked
                    if (r+1, c) not in land:
                        stack.append((r+1, c))
                    if (r-1, c) not in land:
                        stack.append((r-1, c))
                    if (r, c+1) not in land:
                        stack.append((r, c+1))
                    if (r, c-1) not in land:
                        stack.append((r, c-1))
    return islands

                    


        # for each piece of land, add all adjacent/ touching pieces to a dictionary using a stack or recursion
        # increment the island count
    # return the island count


if __name__ == "__main__":

    grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    print(num_islands(grid))

    grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]

    print(num_islands(grid))


