class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = Counter(tasks)
        time = 0
        q = deque()
        heap = [-c for t, c in task_count.items()]
        heapq.heapify(heap)

        while heap or q:
            time += 1

            if heap:
                num = heapq.heappop(heap) + 1
                if num != 0:
                    q.append((time + n, num))

            if q and q[0][0] == time:
                heapq.heappush(heap, q.popleft()[1])

            
        return time


        