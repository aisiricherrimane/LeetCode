class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        for low, high in sorted(intervals):
            if not res:
                res.append([low, high])
            prevH = res[-1][1]
            if prevH >= low:
                res[-1][1] = max(high, prevH)
            else:
                res.append([low, high])
        return res
        