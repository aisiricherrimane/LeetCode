class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()

        for i in range(1, len(intervals)):
            prev_end = intervals[i - 1][1]

            if prev_end > intervals[i][0]:
                return False
        return True
        