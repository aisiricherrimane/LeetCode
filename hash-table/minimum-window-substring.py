class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        counT = {}
        window = {}
        l = 0

        for i in t:
            counT[i] = 1 + counT.get(i, 0)

        have = 0
        need = len(counT)
        res = [-1, -1]
        resl = float('inf')

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in counT and window[c] == counT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resl:
                    res = [l, r]
                    resl = min(resl, r - l + 1)
                window[s[l]] -= 1
                if s[l] in counT and window[s[l]] < counT[s[l]]:
                    have -= 1
                l += 1
        l,r = res
        return s[l:r + 1] if resl != float('inf') else ""
            
            
        