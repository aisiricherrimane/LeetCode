class Solution:
    def decodeString(self, s: str) -> str:
        numStack = []
        charStack = []
        curr_str = ''
        curr_num = 0

        for char in s:
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            
            elif char == '[':
                numStack.append(curr_num)
                charStack.append(curr_str)
                curr_num = 0
                curr_str = ''
            
            elif char ==']':
                num = numStack.pop()
                prev_str = charStack.pop()
                curr_str = prev_str + (curr_str * num)
            
            else:
                curr_str += char
        return curr_str
