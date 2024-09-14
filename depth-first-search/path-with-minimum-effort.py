class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row = len(heights)
        col = len(heights[0])
        
        minH = [[0, 0, 0]] #effort till now, row, col
        visit = set()
        dire = [(0, 1), (1, 0), (-1, 0),(0, -1)]
        while minH:
            effort, r, c = heapq.heappop(minH)
            if (r, c) in visit:
                continue
            if r == row - 1 and c == col - 1:
                return effort
            visit.add((r,c))
            for dr, dc in dire:
                if dr + r >=  0 and dc + c >= 0 and dr + r < row and dc + c < col and (dr + r,dc + c) not in visit:
                    temp_H = abs(heights[r][c] - heights[dr + r][dc + c])
                    heapq.heappush(minH,[max(effort, temp_H), r + dr, c + dc])



        