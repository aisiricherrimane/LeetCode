class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat
        m = len(mat)
        n = len(mat[0])

        flat_list = [num for row in mat for num in row]
        reshape = []

        for i in range(r):
            start = i * c
            end = (i + 1) * c
            row = flat_list[start:end]
            reshape.append(row)
        return reshape

        