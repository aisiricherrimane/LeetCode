class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        par = [i for i in range(n)]
        child = [1] * n

        def find(n):
            n = par[n]
            while n != par[n]:
                par[n] = par[par[n]]
                n = par[n]
            return n
        
        def union(n1, n2):
            p1, p2 = par[n1], par[n2]

            if par[p1] == par[p2]:
                return False

            if par[p1] != par[n2]:
                if child[p1] > child[p2]:
                    child[p1] += 1
                    par[p2] = p1
                else:
                    child[p2] += 1
                    par[p1] = p2
            return True
        
        for u, v in edges:
            if not union(u, v):return False
        return True
