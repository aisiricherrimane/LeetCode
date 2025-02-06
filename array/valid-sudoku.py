class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != '.' and board[r][c] not in row[r] and board[r][c] not in col[c] and board[r][c] not in square[r//3, c//3]:
                    row[r].add(board[r][c])
                    col[c].add(board[r][c])
                    square[r//3, c//3].add(board[r][c])

                elif board[r][c] == '.':
                    continue
                else:
                    return False
        return True

                
        