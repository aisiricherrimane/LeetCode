
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        heap = []
        heapq.heappush(heap, intervals[0][1])

        for i in intervals[1:]:
            heapq.heappush(heap, i[1])
            if heap and heap[0] <= i[0]:
                heapq.heappop(heap)
        return len(heap)
            
