class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count = len(intervals)

        for i in range(1, len(intervals)):
            prev_end = intervals[i - 1][1]
            if prev_end < intervals[i][0]:
                count -= 1
        return count
        
        