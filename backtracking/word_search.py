# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

def exist(board: list[list[str]], word: str) -> bool:
    def dfs(row, col, k):
        if k == len(word):
            return True
        if (not (0<= row <= len(board)-1) or not(0<= col<= len(board[0])-1) or board[row][col] != word[k]):
            return False
        store = board[row][col]
        board[row][col] = "/"
        res = dfs(row+1, col, k+1) or dfs(row, col+1, k+1) or dfs(row-1, col, k+1) or dfs(row, col-1, k+1)
        board[row][col]= store
        return res
    for row in range(len(board)):
        for col in range(len(board[0])):
            if dfs(row, col, 0):
                return True
    return False

if __name__ == "__main__":
    word = "ABCB"
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    print(exist(board, word))