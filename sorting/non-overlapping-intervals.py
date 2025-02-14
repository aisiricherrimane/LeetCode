class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        count = 0

        last_end = intervals[0][1]

        for s, e in intervals[1:]:
            if s < last_end:
                count += 1
                last_end = min(last_end, e)
            else:
                last_end = e
        return count

        