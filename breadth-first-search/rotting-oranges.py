class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        time = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    R, C = dr + r, dc + c
                    if 0 <= R < rows and 0 <= C < cols and grid[R][C] == 1:
                        grid[R][C] = 2
                        q.append((R, C))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1


        