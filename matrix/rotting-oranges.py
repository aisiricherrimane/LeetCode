class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        time = 0
        good = 0
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    good += 1

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q and good > 0:
            for i in range(len(q)):
                R, C = q.popleft()
                for dr, dc in directions:
                    newR, newC = R + dr, C + dc
                    if 0 <= newR < rows and 0 <= newC < cols and grid[newR][newC] == 1:
                        grid[newR][newC] = 2
                        q.append((newR, newC))
                        good -= 1
            time += 1
        return time if good == 0 else -1

                

        