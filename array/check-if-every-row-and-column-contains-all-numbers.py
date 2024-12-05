class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        check = set(i for i in range(1, len(matrix) + 1))
        n = len(matrix)

        for r in range(n):
            row_set = set()
            col_set = set()
            for c in range(n):
                row_set.add(matrix[r][c])
                col_set.add(matrix[c][r])
            if row_set != check or col_set != check:
                return False
        return True
                

         
        