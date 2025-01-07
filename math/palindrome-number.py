class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        temp = x
        compare = 0
        while temp:
            compare = compare * 10 + temp % 10
            temp = temp // 10
        return compare == x
        