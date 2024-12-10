class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        check = set(i for i in range(1, len(matrix) + 1))

        for r in range(len(matrix)):
            rows_set = set()
            cols_set = set()
            for c in range(len(matrix)):
                rows_set.add(matrix[r][c])
                cols_set.add(matrix[c][r])
            if rows_set != check or cols_set != check:
                return False
        return True
                
        