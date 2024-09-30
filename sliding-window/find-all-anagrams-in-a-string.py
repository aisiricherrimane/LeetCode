class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        p_len = len(p)
        p_count = Counter(p)
        s_count = Counter()

        for i in range(len(s)):
            s_count[s[i]] += 1

            if i >= p_len:
                if s_count[s[i - p_len]] == 1:
                    del s_count[s[i - p_len]]  # Remove character count if it becomes zero
                else:
                    s_count[s[i - p_len]] -= 1
            
            if s_count == p_count:
                res.append(i - p_len + 1)  # Start index of the anagram

        return res