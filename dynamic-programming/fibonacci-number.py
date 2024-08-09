class Solution:
    def fib(self, n: int) -> int:
        first=0
        second =1
        if n==0:
            return 0
        if n==1:
            return 1
        for i in range(2,n+1):
            result=first + second
            first=second
            second= result
        return result
        