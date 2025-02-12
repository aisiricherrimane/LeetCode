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
            p1, p2 = find(n1), find(n2)

            if p1 != p2:
                return False
            
            if child[p1] > child[p2]:
                child[p1] += 1
                par[p2] = p1
            else:
                child[p2] += 1
                par[p1] = p2
            return True

        temp = n
        for u1, u2 in edges:
            if not union(u1, u2):
                temp -= 1
        return temp

