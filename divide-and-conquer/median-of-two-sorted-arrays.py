class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2

        if len(B) < len(A):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2
        l = 0
        r = len(A) - 1

        while True:
            i = (l + r) // 2
            j = half - i - 2

            ALeft = A[i] if i >= 0 else float('-inf')
            ARight = A[i + 1] if (i + 1) < len(A) else float('inf')
            BLeft = B[j] if j >= 0 else float('-inf')
            BRight = B[j + 1] if (j + 1)  >= 0 else float('inf')

            if ALeft <= BRight and BLeft <= ARight:
                if total % 2 == 0:
                    return (min(ARight, BRight) + max(ALeft, BLeft)) / 2
                else:
                    return min(ARight, BRight)
            if ALeft >= BRight:
                r = i - 1
            else:
                l = i + 1
                



        