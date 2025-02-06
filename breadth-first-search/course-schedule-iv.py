class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i:[] for i in range(numCourses)}

        for p, c in prerequisites:
            adj[c].append(p)
        
        
        
        def dfs(crs, check):
            if crs == check:
                return True
            for neiN in adj[crs]:
                if dfs(neiN, check):
                    return True
            else:
                return False

        res = []
        for p, c in queries:
            res.append(dfs(c, p))
        return res
        