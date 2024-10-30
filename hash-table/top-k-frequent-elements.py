class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for i in range(len(nums) + 1)]
        temp = {}
        for i in nums:
            temp[i] = 1 + temp.get(i, 0)
        for n, c in temp.items():
            count[c].append(n)

        res = []
        while k:
            for i in range(len(count) - 1, -1, -1):
                for v in count[i]:
                    res.append(v)
                    k -= 1
                    if k == 0:
                        return res
        


        