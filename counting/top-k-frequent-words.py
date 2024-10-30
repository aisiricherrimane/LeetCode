class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
       
        heap = []
        for word, freq in cnt.items():
            heapq.heappush(heap, (-freq, word))
        res = []
        while k:
            res.append(heappop(heap)[1])
            k -= 1
        return res

        
        