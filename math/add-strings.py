class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        length = max(len(num1), len(num2))
        res = ''
        carry = 0
        num1 = num1[::-1]
        num2 = num2[::-1]

        for i in range(length):
            if i < len(num1):
                n1 = int(num1[i])
            else:
                n1 = 0
            
            if i < len(num2):
                n2 = int(num2[i])
            else:
                n2 = 0
            
            digit = n1 + n2 + carry
            carry = digit // 10
            digit = digit % 10
            res = res + str(digit)
        return res[::-1]



