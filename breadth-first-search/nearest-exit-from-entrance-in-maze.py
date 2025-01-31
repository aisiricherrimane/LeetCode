class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        q = deque()
        q.append(entrance)
        visit = set()
        visit.add((entrance[0], entrance[1]))
        row = len(maze)
        col = len(maze[0])
        step = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                if (r, c) != (entrance[0], entrance[1]) and (r in [0, row - 1] or c in [0, col - 1]):
                    return step

                for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < row and 0 <= nc < col and (nr, nc) not in visit and maze[nr][nc] == '.':
                        q.append((nr, nc))
                        visit.add((nr, nc))
                
            step += 1
        return -1