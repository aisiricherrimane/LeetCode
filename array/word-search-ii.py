class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []

        rows = len(board)
        cols = len(board[0])

        def capture(word):
            def dfs(r, c, ind):
                if ind == len(word):
                    return True
                if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[ind]:
                    return False
                letter = board[r][c]
                board[r][c] = ''
                found = dfs(r + 1, c, ind + 1) or dfs(r - 1, c,ind + 1) or dfs(r, c + 1,ind + 1) or dfs(r, c - 1,ind + 1)
                board[r][c] = letter
                return found
            for r in range(rows):
                for c in range(cols):
                    if board[r][c] == word[0]:
                        if dfs(r, c, 0):
                            return True
            return False


        for word in words:
            if capture(word):
                res.append(word)
        return res
        