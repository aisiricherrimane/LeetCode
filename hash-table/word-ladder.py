class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = defaultdict(list)
        wordList.append(beginWord)

        if endWord not in wordList:
            return 0
        
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i + 1:]
                adj[pattern].append(word)

        q = deque()
        q.append(beginWord)
        visit = set()

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word in visit:
                    continue
                if word == endWord:
                    return len(visit) - 1
                visit.add(word)
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i + 1:]
                    for neiW in adj[pattern]:
                        q.append(neiW)



            


        