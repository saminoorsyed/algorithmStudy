# Here queries come in sets of 4, row1, col1 and row2, col2. this outlines a rectangle in which the rows and columns within should be incremented

# the example creates a three by matrix with an initial state of 0 for each space. the top left and bottom right of the of the outlined areas is incremented and the space directly outside is decremented both vertical and horizontally. from there, you loop through the new matrix setting each current value += the previous value. resulting int the appropriate spaces being incremented

def rangeAddQueries(n: int, queries: list[list[int]]) -> list[list[int]]:
    grid = [[0]*n for _ in range(n)]

    for row1, col1, row2, col2 in queries:
        grid[row1][col1] += 1

        if row2 + 1 < n:
            grid[row2+1][col1] -= 1
        if col2 + 1 < n:
            grid[row1][col2+1] -= 1

        if row2 + 1 < n and col2 + 1 < n:
            grid[row2+1][col2+1] += 1

    for i in range(1, n):
        for j in range(n):
            grid[i][j] += grid[i-1][j]
    for i in range(n):
        for j in range(1, n):
            grid[i][j] += grid[i][j-1]
    return grid


if __name__ == "__main__":
    n = 3
    queries = [[1, 1, 2, 2], [0, 0, 1, 1]]
    print(rangeAddQueries(n, queries))
