class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        check = set(i for i in range(1, len(matrix) + 1))
        for r in range(len(matrix)):
            rows = set()
            cols = set()
            for c in range(len(matrix)):
                rows.add(matrix[r][c])
                cols.add(matrix[c][r])
            if rows != check or cols != check:
                return False
        return True
                

         
        