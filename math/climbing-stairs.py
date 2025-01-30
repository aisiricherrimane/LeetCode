class Solution:
    def climbStairs(self, n: int) -> int:
        n2 = 0
        n1 = 1

        for _ in range(n):
            temp = n1
            n1 = n1 + n2
            n2 = temp
        return n1
