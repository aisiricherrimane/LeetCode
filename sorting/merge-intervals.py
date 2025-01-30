class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = [intervals[0]]

        for i in intervals[1:]:
            if i[0] < res[-1][1]:
                res[-1] = (min(i[0], res[-1][0]),max(i[1], res[-1][1]))
            res.append(i)
        return res
        