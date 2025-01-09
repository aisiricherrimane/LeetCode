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
            r, c = q.popleft()
            for tr, tc in [(1, 0), (-1 ,0 ), (0, 1), (0, -1)]:
                dr, dc = tr + r, tc + c
                if dr >= 0 and dr < rows and dc >= 0 and dc < cols and rooms[dr][dc] == 2147483647:
                    rooms[dr][dc] = rooms[r][c] + 1
                    q.append((dr, dc))
        
        


        