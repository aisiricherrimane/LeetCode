class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj ={c:[] for word in words for c in word}

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            t = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:t] == word2[:t]:
                    return ''
            for j in range(t):
                if word1[j] != word2[j]:
                    adj[word1[j]].append(word2[j])
                    break
        visited = {}
        res = []
        def dfs(letter):
            if letter in visited:
                return visited[letter]
            visited[letter] = True

            for nextL in adj[letter]:
                if dfs(nextL):
                    return True
            visited[letter] = False
            res.append(letter)
        
        for l in adj:
            dfs(l)
        res.reverse()
        return ''.join(res)