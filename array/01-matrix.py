class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    q.append([r, c])
                elif mat[r][c] == 1:
                    mat[r][c] = -1
        dirc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while q:
            r, c = q.popleft()
            for dr, dc in dirc:
                R, C = dr + r, dc + c
                if 0 <= R < rows and 0 <= C < cols and mat[R][C] == -1:
                    mat[R][C] = mat[r][c] + 1
                    q.append((R, C))
        return mat

