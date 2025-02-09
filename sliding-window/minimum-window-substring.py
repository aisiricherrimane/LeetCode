class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ''
        countT = Counter(t)
        window = {}

        res = [-1, -1]
        resl = float(inf)

        have = 0
        need = len(countT)

        l = 0
        for r in range(len(s)):
            letter = s[r]
            window[letter] = 1 + window.get(letter, 0)

            if letter in countT and window[letter] == countT[letter]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resl:
                    resl = r - l + 1
                    res = [l , r]
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r + 1]


        