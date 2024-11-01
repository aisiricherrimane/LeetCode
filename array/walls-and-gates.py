class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows = len(rooms)
        cols = len(rooms[0])
        q = deque()
        visit = set()
        dist = 0

        def bfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visit or rooms[r][c] == -1:
                return
            visit.add((r, c))
            q.append([r, c])
        
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))
        while q:
            for i in range(len(q)):
                R, C = q.popleft()
                rooms[R][C] = dist
                bfs(R + 1, C)
                bfs(R - 1, C)
                bfs(R, C + 1)
                bfs(R, C - 1)
            dist += 1


            
        