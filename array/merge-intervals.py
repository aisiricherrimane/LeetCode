class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = [intervals[0]]
        intervals.pop(0)

        for i in intervals:
            if i[0] <= res[-1][1]:
                res[-1][1] = max(i[1], res[-1][1])
            else:
                res.append(i)
        return res