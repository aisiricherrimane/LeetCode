class Solution:
    def climbStairs(self, n: int) -> int:
        num1 = num2 = 1
        for n in range(n - 1):
            temp = num1
            num1 = num2
            num2 = num1 + temp
        return num2
        