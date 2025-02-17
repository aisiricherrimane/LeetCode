class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}

        for p, c in prerequisites:
            adj[c].append(p)
        
        res = []
        visited = set()
        cycle = set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            cycle.add(crs)
            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            res.append(crs)
            cycle.remove(crs)
            visited.add(crs)

        for c in range(numCourses):
            dfs(c)
        
        return res
        