class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        if beginWord not in wordList:
            wordList.append(beginWord)

        temp = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i + 1:]
                temp[pattern].append(word)

        q = deque()
        q.append(beginWord)
        visit = set()
        visit.add(beginWord)
        res = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return res

                visit.add(word)

                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i + 1:]
                    for neiW in temp[pattern]:
                        if neiW not in visit:
                            q.append(neiW)
    
            res += 1
        return 0

