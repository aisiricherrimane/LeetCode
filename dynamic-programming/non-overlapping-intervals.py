class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0

        last_end = intervals[0][1]

        for s, e in intervals[1:]:
            if s < last_end:
                count += 1
            else:
                last_end = e
        return count

        