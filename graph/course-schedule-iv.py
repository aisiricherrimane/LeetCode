class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i: [] for i in range(numCourses)}
        for u, v in prerequisites:
            adj[v].append(u)
        
        premap = defaultdict(set)
        def dfs(crs):
            if crs not in premap:
                for c in adj[crs]:
                    premap[crs] |= dfs(c) #since we are using set can use extaned and add all so using | whihcg acts as union function
                premap[crs].add(crs)
            return premap[crs]
            
        for crs in range(numCourses):
            dfs(crs)
        res = []
        for c1, c2 in queries:
            res.append(c1 in premap[c2])
        return res
                