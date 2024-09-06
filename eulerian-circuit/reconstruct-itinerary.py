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
            
            temp = adj[dst][:]  # Copy current list of destinations
            for i, place in enumerate(temp):
                adj[dst].pop(i)  # Remove destination from adjacency list
                res.append(place)  # Add the destination to the result
                if dfs(place):  # Recursive DFS call
                    return True
                adj[dst].insert(i, place)  # Backtrack by reinserting the place
                res.pop()  # Backtrack by removing the place from result
            return False
            
        dfs("JFK")
        return res