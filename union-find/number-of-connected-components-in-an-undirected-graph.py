class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        child = [1] * n

        def find(n):
            n = par[n]
            while n != par[n]:
                par[n] = par[par[n]]
                n = par[n]
            return n
        
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return False

            if child[p1] > child[p2]:
                child[p1] += 1
                par[p2] = p1
            else:
                child[p2] += 1
                par[p1] = p2
            return True

        res = n
        for u, v in edges:
            if union(u, v):
                res -= 1
        return res

     