class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            adj[crs].append(pre)

        visit = set()
        visited = set()
        output = []

        def dfs(crs):
            if crs in visited:
                return True
            if crs in visit:
                return False
            visit.add(crs)
            for nei in adj[crs]:
                if not dfs(nei): return False
            visit.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return output
        