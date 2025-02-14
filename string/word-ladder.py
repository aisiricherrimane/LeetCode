class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        if beginWord not in wordList:
            wordList.append(beginWord)
        
        adj = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i + 1:]
                adj[pattern].append(word)

        q = deque([beginWord])
        length = 1
        visit = set()
        
        while q:
            for _ in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return length
                if word in visit:
                    continue
                visit.add(word)
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i + 1:]
                    for same_pattern_word in adj[pattern]:
                        q.append(same_pattern_word)


            length += 1
        return 0
                
