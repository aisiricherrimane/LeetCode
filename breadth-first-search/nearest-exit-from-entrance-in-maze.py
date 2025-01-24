class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        q = deque([(entrance[0], entrance[1], 0)])
        visit = set()
        visit.add((entrance[0], entrance[1]))
        rows = len(maze)
        cols = len(maze[0])

        while q:
            r, c, steps = q.popleft()
            
            if (r, c) != (entrance[0], entrance[1]) and (r in [0, rows - 1] or c in [0, cols - 1]):
                return steps

            for dr, dc in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                newR, newC = r + dr, c + dc
                if 0 <= newR < rows and 0 <= newC < cols and maze[newR][newC] == '.' and (newR, newC) not in visit:
                    visit.add((newR, newC))
                    q.append((newR, newC, steps + 1))

        
        return -1  # If no exit is reachable
            


        