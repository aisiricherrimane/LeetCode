class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        rows = len(maze)
        cols = len(maze[0])

        visit = set()
        q = deque([start])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                if [r, c] == destination:
                    return True
                
                if (r, c) in visit:
                    continue

                visit.add((r, c))
                
                for dr, dc in directions:
                    nr, nc = r, c

                    while 0 <= nr + dr < rows and 0 <= nc + dc < cols and maze[nr + dr][nc + dc] == 0:
                        nr += dr
                        nc += dc
                    
                    if (nr, nc) not in visit:
                        q.append((nr, nc))
            

        return False





        