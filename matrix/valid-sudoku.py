class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        square = collections.defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue
                val = board[r][c]
                if val not in rows[r] and val not in cols[c] and val not in square[(r//3, c//3)]:
                    rows[r].add(val)
                    cols[c].add(val)
                    square[(r//3, c//3)].add(val)
                else:
                    return False
        return True



        