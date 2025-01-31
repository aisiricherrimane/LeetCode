class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}

        for p, c in prerequisites:
            adj[c].append(p)

        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            if adj[crs] == []:
                return True

            visit.add(crs)

            for pre in adj[crs]:
                if not dfs(pre): 
                    return False
                    
            adj[crs] = []
            visit.remove(crs)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        