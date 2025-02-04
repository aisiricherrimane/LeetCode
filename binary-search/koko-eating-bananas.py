class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l < r:
            hours = 0
            mid = (l + r) // 2

            for p in piles:
                hours += math.ceil(p / mid)

            if hours <= h:
                r = mid
            else:
                l = mid + 1
        return r
            
            

        