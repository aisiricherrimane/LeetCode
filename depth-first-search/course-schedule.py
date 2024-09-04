class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preq_map = {i:[] for i in range(numCourses)}

        for c, p in prerequisites:
            preq_map[c].append(p)

        visit = set()

        def dfs(course):
            if course in visit:
                return False
            if preq_map[course] == []:
                return True
            visit.add(course)
            for p in preq_map[course]:
                if not dfs(p): return False
            visit.remove(course)
            preq_map[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
            
            

        