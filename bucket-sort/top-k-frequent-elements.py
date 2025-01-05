class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]
        for num, c in count.items():
            freq[c].append(num)
        
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for char in freq[i]:
                res.append(char)
                k -= 1
                if k == 0:
                    return res

      