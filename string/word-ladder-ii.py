from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        
        # Create adjacency list for patterns
        wordList.append(beginWord)
        adj = defaultdict(list)
        for word in wordList:
            for w in range(len(word)):
                pattern = word[:w] + '*' + word[w + 1:]
                adj[pattern].append(word)
        
        # BFS setup
        q = deque([(beginWord, [beginWord])])  # Store current word and path to that word
        res = []
        visit = set([beginWord])  # Track visited words
        found = False
        local_visited = set()  # Track words visited at current level
        
        while q and not found:
            for _ in range(len(q)):
                curr_word, path = q.popleft()
                
                if curr_word == endWord:
                    res.append(path)
                    found = True
                
                for i in range(len(curr_word)):
                    pattern = curr_word[:i] + '*' + curr_word[i + 1:]
                    for word in adj[pattern]:
                        if word not in visit:
                            q.append((word, path + [word]))  # Create a new path
                            local_visited.add(word)
            
            visit.update(local_visited)
            local_visited.clear()
        
        return res
