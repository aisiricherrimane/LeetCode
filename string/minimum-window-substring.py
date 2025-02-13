class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        window = {}

        need = len(count_t)
        have = 0

        resl = float('inf')
        resp = [-1, -1]

        l = 0
        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char, 0)

            if char in count_t and window[char] == count_t[char]:
                have += 1
            
            while have == need:
                if resl > r - l + 1:
                    resl = r - l + 1
                    resp = [l, r]
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
        l, r = resp
        return s[l:r+1]