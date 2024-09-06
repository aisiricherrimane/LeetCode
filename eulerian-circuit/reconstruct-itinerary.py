class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src: [] for src, dst in tickets}
        res = []

        for src, dst in tickets:
            adj[src].append(dst)

        for key in adj:
            adj[key].sort()

        res = ["JFK"]

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False

            temp = adj[src][:]
            for i, p in enumerate(temp):
                adj[src].pop(i)
                res.append(p)
                if dfs(p):
                    return True
                adj[src].insert(i, p)
                res.pop()
            return False
        dfs("JFK")
        return res



      










        
        


                