class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preq_map = {i: [] for i in range(numCourses)}

        # Build the adjacency list for prerequisites
        for c, p in prerequisites:
            preq_map[c].append(p)

        visit = set()   # Tracks the nodes currently in the DFS path (cycle detection)
        visited = set() # Tracks nodes that have been fully processed

        def dfs(course):
            if course in visit:  # If the course is already in the current path, cycle detected
                return False
            if course in visited: # If the course is fully processed, skip
                return True

            visit.add(course)
            for p in preq_map[course]:
                if not dfs(p):
                    return False
            
            visit.remove(course) # Remove from current path since it's fully processed
            visited.add(course)  # Mark as fully processed
            return True

        # Perform DFS for each course
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True
