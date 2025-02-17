class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i:[] for i in range(numCourses)}

        for p, c in prerequisites:
            adj[c].append(p)

        premap = defaultdict(set)

        def dfs(crs):
            if crs not in premap:
                for c in adj[crs]:
                    premap[crs] |= dfs(c)
                premap[crs].add(crs)
            return premap[crs]

        for c in range(numCourses):
            dfs(c)
        res = []
        for p, c in queries:
            res.append(p in premap[c])
        return res
        