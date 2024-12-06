class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_l = len(p)
        s_count = Counter(s[:p_l - 1])
        p_count = Counter(p)
        res = []

        for r in range(p_l - 1, len(s)):
            s_count[s[r]] += 1

            if s_count == p_count:
                res.append(r - p_l + 1)
            
            s_count[s[r - p_l + 1]] -= 1
            if s_count[s[r - p_l]] == 0:
                del s_count[s[r - p_l]]
        return res





        