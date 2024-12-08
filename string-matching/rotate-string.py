class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(goal) != len(s):
            return False
        temp = s + s

        for i in range(len(s)):
            if temp[i:i + len(s)] == goal:
                return True
        return False
            


        
        