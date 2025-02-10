
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()  
        rooms = []  
        heapq.heappush(rooms, intervals[0][1]) 

        for i in intervals[1:]:
            heapq.heappush(rooms, i[1])
            if rooms[0] <= i[0]:
                heapq.heappop(rooms)  # Remove ended meeting from heap

        return len(rooms)  #

