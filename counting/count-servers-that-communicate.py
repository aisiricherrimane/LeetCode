class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        last_server_in_row = [-1] * len(grid)
        server_in_col = [0] * len(grid[0])
        communicating_servers = 0

        for r in range(len(grid)):
            good_servers = 0
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    good_servers += 1
                    server_in_col[c] += 1
                    last_server_in_row[r] = c
            
            if good_servers > 1:
                communicating_servers += good_servers
                last_server_in_row[r] = -1
        
        for r in range(len(grid)):
            if last_server_in_row[r] != -1 and server_in_col[last_server_in_row[r]] > 1:
                communicating_servers += 1
        
        return communicating_servers




        