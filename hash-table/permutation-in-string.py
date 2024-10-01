class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = Counter(s1)
        l1 = len(s1)
        l2 = len(s2)

        window = Counter(s2[:l1])

        if l1 > l2:
            return False

        if window == count_s1:
            return True

        for i in range(l1,l2):
            window[s2[i]] += 1

            window[s2[i - l1]] -= 1

            if window[s2[i - l1]] == 0:
                del window[s2[i - l1]]
            
            if window == count_s1:
                return True
        return False
            
        