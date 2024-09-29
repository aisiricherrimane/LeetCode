class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            if r >= 0 and r < row and c >= 0 and c < col and board[r][c] == word[i]:
                letter = board[r][c]
                board[r][c] = ""
                found = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)
                board[r][c] = letter
                return found
            
        i = 0
        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0]:
                    if dfs(r, c, i):
                        return True
        return False

        