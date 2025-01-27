class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        
        p1 = p2 = 0

        while p1 < len(slots1) and p2 < len(slots2):
            in_right = min(slots1[p1][1], slots2[p2][1])
            in_left = max(slots1[p1][0], slots2[p2][0])

            if in_right - in_left >= duration:
                return [in_left, in_left + duration]
            
            if slots1[p1][1] < slots2[p2][1]:
                p1 += 1
            else:
                p2 += 1
        return []