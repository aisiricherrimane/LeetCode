class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        

        store = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i + 1:]
                store[pattern].append(word)

        q = deque()
        q.append(beginWord)
        visit = set()
        visit.add(word)
        length = 1

        while q:
            for _ in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return length

                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i + 1:]
                    for neiW in store[pattern]:
                        if neiW not in q:
                            q.append(neiW)
                            visit.add(word)
            length += 1
        
                            
        

        