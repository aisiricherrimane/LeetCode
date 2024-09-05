class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i : [] for i in range(numCourses)}
        
        for crs, pre in prerequisites:
            adj[crs].append(pre)

        visit = set()
        def dfs(course):
            if course in visit:
                return False
            if adj[course] == []:
                return True
            visit.add(course)
            for pre in adj[course]:
                if not dfs(pre):
                    return False
            adj[course] = []
            visit.remove(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
