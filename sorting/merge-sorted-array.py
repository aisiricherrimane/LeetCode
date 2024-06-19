class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index1, index2, insertIndex = m - 1, n - 1, m + n - 1

 
        while index2 >= 0:
           
            if index1 >=0 and nums1[index1] > nums2[index2]:
                nums1[insertIndex] = nums1[index1]
                index1 -= 1
            else:
                nums1[insertIndex] = nums2[index2]
                index2 -= 1

            insertIndex -= 1