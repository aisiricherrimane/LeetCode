class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        currmax = 1
        currmin = 1
        result = nums[0]

        for n in nums:
            if n == 0:
                currmax = 1
                currmin = 1
            temp = currmax * n
            currmax = max(currmax * n, currmin * n, n)
            currmin = min(currmin *n, temp, n)

            result = max(result, currmax, currmin)
        return result


        