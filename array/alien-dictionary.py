class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            minL = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minL] == w2[:minL]:
                return ''
            for j in range(minL):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visited = {}
        res = []
        
        def dfs(c):
            if c in visited:
                return visited[c]
            
            visited[c] = True
            for neiC in adj[c]:
                if dfs(neiC):
                    return True
            visited[c] = False
            res.append(c)
    
        for char in adj:
            if dfs(char):
                return ''
        res.reverse()
        return ''.join(res)
            

        
            
                    