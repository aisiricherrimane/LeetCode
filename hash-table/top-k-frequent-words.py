class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        heap = []
        for word, c in cnt.items():
            heapq.heappush(heap, [-1 * c, word])
        res = []
        while k > 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1

        return res
        
        