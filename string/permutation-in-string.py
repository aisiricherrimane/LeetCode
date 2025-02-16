class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
       l_s1 = len(s1)
        l_s2 = len(s2)
        count_s1 = Counter(s1)
        window = Counter(s2[:l_s1])

        if count_s1 == window:
            return True
        
        for i in range(l_s1, l_s2):
            window[s2[i - l_s1]] -= 1
            window[s2[i]] += 1

            if window == count_s1:
                return True
        return False
