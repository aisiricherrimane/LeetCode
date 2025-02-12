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
                    q.append((r, c, 0))

        visit = set()

        while q:
            for _ in range(len(q)):
                r, c, a = q.popleft()

                if (r, c) in visit:
                    return 
                visit.add((r, c))
                rooms[r][c] = a

                for dr, dc in [[0, 1] , [0, -1] , [1, 0], [-1, 0]]:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == 2147483647:
                        q.append((nr, nc, a + 1))
        return rooms
