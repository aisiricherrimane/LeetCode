class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src : [] for src, dst in tickets}

        for src, dst in tickets:
            adj[src].append(dst)

        for key in adj:
            adj[key].sort()

        res = ['JFK']
        
        def dfs(dst):
            if len(res) == len(tickets) + 1:
                return True
            if dst not in adj:
                return False
            
            temp = adj[dst][:]
            for i, place in enumerate(temp):
                adj[dst].pop(i)
                res.append(place)
                if dfs(place):
                    return True
                adj[src].insert(i, place)
                res.pop()
            return False
        dfs("JFK")
        return res