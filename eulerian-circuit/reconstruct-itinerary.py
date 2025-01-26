class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {s:[] for s, e in tickets}

        for s, d in tickets:
            adj[s].append(d)
        
        for key in adj:
            adj[key].sort()
        

        res = ['JFK']

        def dfs(dst):
            if len(res) == len(tickets) + 1:
                return True
            
            if dst not in adj:
                return False
            
            temp = list(adj[dst])

            for i, v in enumerate(temp):
                adj[dst].pop(i)
                res.append(v)

                if dfs(v):
                    return True
                
                adj[dst].insert(i, v)
                res.pop()
            return False

        return res if dfs('JFK') else False


