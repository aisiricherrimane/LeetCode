class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows = len(rooms)
        cols = len(rooms[0])
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append((r, c))
        
        while q:
            r, c  = q.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                R, C = dr + r, dc + c
                if 0 <= R < rows and 0 <= C < cols and rooms[R][C] == 2147483647:
                    rooms[R][C] = rooms[r][c] + 1
                    q.append((R, C))
            

                