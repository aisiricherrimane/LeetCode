class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        nei = collections.defaultdict(list)
        for word in wordList:
            for w in range(len(word)):
                temp = word[:w] + '*' + word[w + 1:]
                nei[temp].append(word)
        res = 1
        visit = set()
        visit.add(beginWord)
        q = deque([beginWord])

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for w in range(len(word)):
                    pattern = word[:w] + '*' + word[w + 1:]
                    for neiW in nei[pattern]:
                        if neiW not in visit:
                            visit.add(neiW)
                            q.append(neiW)
            res += 1

        return 0


        
