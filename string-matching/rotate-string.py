class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        temp = s + s

        for i in range(len(s)):
            if temp[i:i + len(s)] == goal:
                return True
        return False
            


        
        