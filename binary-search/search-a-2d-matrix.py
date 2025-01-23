class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        top = 0
        down = row - 1

        while top <= down:
            mid = (down + top) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                down = mid - 1
            else:
                break
        

        l = 0
        r = col - 1
        while l <= r:
            m = (l + r) // 2
            if target == matrix[mid][m]:
                return True
            elif target > matrix[mid][m]:
                l = m + 1
            elif target < matrix[mid][m]:
                r = m - 1
        return False


