class Solution:
    def myPow(self, x: float, n: int) -> float:
        return self.binExp(x, n)
        
    def binExp(self, x, n):
        if n == 0:
            return 1
        
        if n < 0:
            return 1.0 / self.binExp(x, -1 * n)
        
        if n % 2 == 0:
            return self.binExp(x * x, n // 2)
        else:
            return x * self.binExp(x * x, (n - 1) // 2)

