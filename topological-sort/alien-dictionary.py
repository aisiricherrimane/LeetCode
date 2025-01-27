class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            for j in range(min(len(word1), len(word2))):
                if len(word1) > len(word2) and word1[:min(len(word1), len(word2))] == word2[:min(len(word1), len(word2))]:
                    return ''
                if word1[j] != word2[j]:
                    adj[word1[j]].add(word2[j])
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
        
        for c in adj:
            if dfs(c):
                return ''
        
        res.reverse()
        return ''.join(res)

                
        