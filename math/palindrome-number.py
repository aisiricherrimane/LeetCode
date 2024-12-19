class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        y = 0

        while temp > 0:
            digit = temp % 10
            y = y * 10 + digit
            temp = temp // 10
        return y == x

        