class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        
        """
        if not board or not board[0]:
            return 
        rows = len(board)
        cols = len(board[0])

        def capture(r, c):
            if 0 <= r < rows and 0 <= c < cols and board[r][c] == 'O':
                board[r][c] = 'T'
                capture(r + 1, c)
                capture(r - 1, c)
                capture(r, c + 1)
                capture(r, c - 1)

        
        for r in range(rows):
            for c in [0, cols - 1]:
                if board[r][c] == 'O':
                    capture(r, c)
        for r in [0, rows - 1]:
            for c in range(cols):
                if board[r][c] == 'O':
                    capture(r, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
        