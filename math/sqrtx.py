class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left = 2
        right = x // 2

        while left <= right:
            pivot = (left + right) // 2
            num = pivot * pivot

            if num > x:
                right = pivot - 1
            elif num < x:
                left = pivot + 1
            else:
                return pivot
        return right