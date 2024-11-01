class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_map = {c:[] for c in range(numCourses)}

        for crs, pre in prerequisites:
            course_map[crs].append(pre)
        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            if course_map[crs] == []:
                return True
            visit.add(crs)
            for pre in course_map[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            course_map[crs] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
                
            
