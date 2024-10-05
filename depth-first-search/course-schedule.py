class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjM = {i:[] for i in range(numCourses)}

        for c, p in prerequisites:
            adjM[c].append(p)
        visit = set()
        def dfs(crs):
            if crs in visit:
                return False
            if adjM[crs] == []:
                return True
            visit.add(crs)
            for pre in adjM[crs]:
                if not dfs(pre):
                    return False
            adjM[crs] = []
            visit.remove(crs)
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

        
        