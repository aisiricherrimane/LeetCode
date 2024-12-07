class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for i in range(len(nums) + 1)]
        temp = {}
        for num in nums:
            temp[num] = 1 + temp.get(num, 0)
        
        for n, c in temp.items():
            count[c].append(n)
        
        res = []
        for i in range(len(count) - 1, -1, -1):
            for n in count[i]:
                res.append(n)
                k -= 1
                if k == 0:
                    return res
        
