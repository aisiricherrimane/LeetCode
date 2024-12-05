class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        check = list(i for i in range(1, len(matrix) + 1))
        rows = cols = len(matrix)

        for r in range(rows):
            temp = check[:]
            for c in range(cols):
                if matrix[r][c] in temp:
                    temp.remove(matrix[r][c])
                    continue
                else:
                    return False
        return True
                

         
        