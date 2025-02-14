class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}

        for c, p in prerequisites:
            adj[c].append(p)
        
        res = []
        visited = set()
        cycle = set()

        def dfs(crs):
            if crs in visited:
                return True
            if crs in cycle:
                return False
            cycle.add(crs)

            for pre in adj[crs]:
                if not dfs(pre): return False
            cycle.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True


        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res