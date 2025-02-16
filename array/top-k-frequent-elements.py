class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        k = len(nums) - k

        def quickselect(l, r):
            pivot = nums[r]
            p = l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            
            if len(set(nums[p:])) > k:
                return quickselect(l, p - 1)
                
            elif len(set(nums[p:])) < k:
                return quickselect(p + 1, r)
            else:
                return list(set(nums[p:]))
        
        return quickselect(0, len(nums) - 1)




        