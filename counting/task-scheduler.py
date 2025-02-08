class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = Counter(tasks)
        heap = [-c for t,c in task_count.items()]
        heapq.heapify(heap)
        time = 0
        queue = deque()

        while heap or queue:
            time += 1

            if heap:
                num = heapq.heappop(heap)
                if (num + 1) != 0:
                    queue.append([time + n, num + 1])

            if queue and queue[0][0] == time:
                heapq.heappush(heap, queue.popleft()[1])
        return time


        