class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        top = 0
        right = cols - 1
        bottom = rows - 1

        while left < right:
            for i in range(right - left):
                temp = matrix[top][left + i]

                matrix[top][left + i] = matrix[bottom - i][left]
                matrix[bottom - i][left] = matrix[bottom][right - i]
                matrix[bottom][right - i] = matrix[top + i][right]
                matrix[top + i][right] = temp
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        return matrix
        