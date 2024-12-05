class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preM = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preM[crs].append(pre)

        curr = set()
        visited = set()

        def dfs(crs):
            if crs in curr:
                return False

            if crs in visited:
                return True

            curr.add(crs)
            for p in preM[crs]:
                if not dfs(p): return False

            curr.remove(crs)
            visited.add(crs)
            return True
            
        for c in range(numCourses):
            if not dfs(c): return False
        return True

        
        