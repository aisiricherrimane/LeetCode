class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_map = {i:[] for i in range(numCourses)}

        for c, p in prerequisites:
            course_map[c].append(p)
        
        
        visit = set()
        visited = set()
        output = []
        def dfs(crs):
            if crs in visited:
                return True
            if crs in visit:
                return False
            visit.add(crs)
            for pre in course_map[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return output 

        