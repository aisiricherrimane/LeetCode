class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i:[] for i in range(n)}

        for s, e in edges:
            adj[s].append(e)
            adj[e].append(s)
        
        visit = set()
        def dfs(node, prev):
            if node in visit:
                return False

            visit.add(node)

            for neiN in adj[node]:
                if neiN == prev:
                    continue
                if not dfs(neiN, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visit) == n