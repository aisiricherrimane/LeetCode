class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        temp = {}
        for w in words:
            temp[w] = 1 + temp.get(w, 0)
        minH = []
        for w, c in temp.items():
            heapq.heappush(minH, [-1 * c, w])
        res = []
        while len(res) < k:
            res.append(heapq.heappop(minH)[1])
        return res
        



        