class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        times = len(nums) - k
        while times > 0 and nums:
            heapq.heappop(nums)
            times -= 1
        e = heapq.heappop(nums)

        return e


        