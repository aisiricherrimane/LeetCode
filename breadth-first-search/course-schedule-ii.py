class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}

        for c, p in prerequisites:
            adj[c].append(p)
        
        res = []
        visited = set()
        curr_cycle = set()

        def dfs(crs):
            if crs in curr_cycle:
                return False
            if crs in visited:
                return 
            curr_cycle.add(crs)
            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            curr_cycle.remove(crs)
            visited.add(crs)
            return True
        
        for c in range(numCourses):
            if not dfs:
                return False
            res.append(c)
        return res

        