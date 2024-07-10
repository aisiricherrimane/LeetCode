class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        def helper(i, distance):
            if i < 0 or i >= len(s) or res[i] < distance:
                return 
            res[i] = distance
            helper(i + 1, distance + 1)
            helper(i - 1, distance + 1)
        res = [len(s)] * len(s)
        for i, char in enumerate(s):
            if char == c:
                helper(i, 0)
        return res

        