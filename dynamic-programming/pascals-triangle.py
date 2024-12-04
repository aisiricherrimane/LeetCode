class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for row in range(numRows):
            curr_row = [1]

            if row > 0:
                for col in range(1, row):
                    curr_row.append(triangle[row - 1][col - 1] + triangle[row - 1][col])
                curr_row.append(1)
            triangle.append(curr_row)
        return triangle