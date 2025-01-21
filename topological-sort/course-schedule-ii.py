class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = set()
        current = set()
        adj = {i:[] for i in range(numCourses)}

        for p, c in prerequisites:
            adj[p].append(c)
        print(adj)
        
        def dfs(crs):
            if crs in current:
                return False
            if crs in visited:
                return True
            current.add(crs)
            for p in adj[crs]:
                if not dfs(p):
                    return False
            current.remove(crs)
            visited.add(crs)
            return True

        
        result = []
        for c in range(numCourses):
            if not dfs(c):
                return []
            else:
                result.append(c)
        return result
        