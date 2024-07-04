class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        if len(nums1) < len(nums2):
            for i in nums1:
                if i in nums2:
                    res.add(i)
        else:
            for i in nums2:
                if i in nums1:
                    res.add(i)
        
        return res

        