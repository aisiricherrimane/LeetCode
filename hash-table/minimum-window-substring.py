class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ''
        count_t = Counter(t)
        window = {}

        need = len(count_t)
        have = 0

        resl = float('inf')
        res = [-1, -1]

        l = 0

        for r in range(len(s)):
            char = s[r]

            window[char] = 1 + window.get(char, 0)

            if char in count_t and count_t[char] == window[char]:
                have += 1

            while have == need:
                if r - l + 1 < resl:
                    resl = r - l + 1
                    res = [l, r]
                window[s[l]] -= 1

                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1]
                    
        