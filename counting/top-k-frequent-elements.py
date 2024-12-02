class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        count_dict = {}
        for n in nums:
            count_dict[n] = 1 + count_dict.get(n, 0)
        
        for n, c in count_dict.items():
            freq[c].append(n)
        res = []
        for nos in range(len(freq) - 1, -1, -1):
            for n in freq[nos]:
                res.append(n)
                k -= 1
                if k == 0:
                    return res




        