class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        q = deque()

        def dfs(r, c):
            if 0 <= r < rows and 0 <= c < cols and board[r][c] == 'O':
                board[r][c] = 'T'
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r,c + 1)
                dfs(r, c - 1)

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
                if board[r][c] == 'O':
                    board[r][c] = 'X'

                if board[r][c] == 'T':
                    board[r][c] = 'O'