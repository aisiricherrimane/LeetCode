class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord not in wordList:
            wordList.append(beginWord)
        if endWord not in wordList:
            return 0

        adj = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i + 1:]
                adj[pattern].append(word)
        
        q = deque()
        q.append(beginWord)
        visit = set()
        l = 1

        while q:
            for _ in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return l
                if word in visit:
                    continue
                visit.add(word)

                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i + 1:]
                    for w in adj[pattern]:
                        q.append(w)
            l += 1
        return 0

       