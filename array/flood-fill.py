class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row = len(image)
        col = len(image[0])
        check = image[sr][sc] 
        if check == color:
            return image
        dirc = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(r, c):
            image[r][c] = color
            for dr, dc in dirc:
                R, C = r + dr, c + dc
                if R >= 0 and R < row and C >= 0 and C < col and image[R][C] == check:
                    dfs(R, C)
        dfs(sr, sc)
        return image
             
        