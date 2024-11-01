class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        child = [1] * n

        def find(n):
            if n != par[n]:
                par[n] = find(par[n])  
            return par[n]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            
            if child[p1] > child[p2]:
                child[p1] += 1
                par[p2] = p1
            else:
                child[p2] += 1
                par[p1] = p2
            return 1
        ans = n
        for n1, n2 in edges:
            ans -= union(n1, n2)
        return ans  
