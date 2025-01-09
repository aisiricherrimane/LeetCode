class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        
        """
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c):
            board[r][c] = 'T'
            for dr, dc in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                newr, newc = dr + r, dc + c
                if newr >= 0 and newr < rows and newc >= 0 and newc < cols and board[newr][newc] == 'O':
                    dfs(newr, newc)


        for r in range(rows):
            for c in [0, cols - 1]:
                if board[r][c] == 'O':
                    dfs(r, c)
        for r in [0, rows - 1]:
            for c in range(cols):
                if board[r][c] == 'O':
                    dfs(r, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
        return board
        