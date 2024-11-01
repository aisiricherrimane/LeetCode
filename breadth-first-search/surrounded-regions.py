class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # basci declaration
        rows = len(board)
        cols = len(board[0])

        # dfs
        def dfs(r, c):
            board[r][c] = 'T'
            directions = [(1, 0), (-1, 0), (0, 1), (0 ,-1)]
            for dr, dc in directions:
                nR, nC = dr + r, dc + c
                if nR >= 0 and nR < rows and nC >= 0 and nC < cols and board[nR][nC] == 'O':
                    dfs(nR, nC)

        # for r
        for r in range(rows):
            if board[r][0] == 'O':
                dfs(r, 0)
            elif board[r][cols - 1] == 'O':
                dfs(r, cols - 1)
        # for c
        for c in range(cols):
            if board[0][c] == 'O':
                dfs(0, c)
            elif board[rows - 1][c] == 'O':
                dfs(rows - 1, c)
        
        # compleet traverse
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
        return board
        # return




        