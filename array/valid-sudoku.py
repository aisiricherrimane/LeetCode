class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        square = collections.defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '.' :
                    continue
                if (board[r][c] not in rows[r] and board[r][c] not in cols[c] and board[r][c] not in square[(r//3, c//3)]):
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    square[(r//3, c//3)].add(board[r][c])    
                else:
                    return False
        return True