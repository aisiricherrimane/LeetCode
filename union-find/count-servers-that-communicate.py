class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        comunicating_servers = 0
        last_server_in_row = [-1] * len(grid)
        row = len(grid)
        col = len(grid[0])
        col_count = [0] * col

        for r in range(row):
            good_servers = 0
            for c in range(col):
                if grid[r][c] == 1:
                    good_servers += 1
                    last_server_in_row[r] = c
                    col_count[c] += 1
            
            if good_servers > 1:
                comunicating_servers += good_servers
                last_server_in_row[r] = -1
        
        for r in range(row):
            if last_server_in_row[r]!= -1 and col_count[last_server_in_row[r]] > 1:
                comunicating_servers += 1
        return comunicating_servers
            