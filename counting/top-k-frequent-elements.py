class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = {}
        for n in nums:
            temp[n] = 1 + temp.get(n, 0)

        count = [[] for i in range(len(nums) + 1)]
        
        for n, c in temp.items():
            count[c].append(n)
        
        res = []
        for c in range(len(count) - 1, 0, -1):
            for n in count[c]:
                if k != 0:
                    res.append(n)
                    k -= 1
        return res





        