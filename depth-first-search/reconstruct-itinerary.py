class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        tickets.sort()

        for s,d in tickets:
            adj[s].append(d)
        
        res = ['JFK']
        def dfs(city):
            if len(res) == len(tickets)+1:
                return True
            if city not in adj:
                return False
            temp = list(adj[city])
            for i, nc in enumerate(temp):
                adj[city].pop(i)
                res.append(nc)

                if dfs(nc):
                    return True
                adj[city].insert(i, nc)
                res.pop()
            return False
        dfs('JFK')
        return res
                

    

        