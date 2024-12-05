class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        check = set(i for i in range(1, len(matrix) + 1))
        rows = cols = len(matrix)

        for r in range(rows):
            temp = set()
            for c in range(cols):
                temp.add(matrix[r][c])
            if temp != check:
                return False
        return True
                

         
        