class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        stack = []

        for x in asteroids:
            if x > 0:
                stack.append(x)
            else:
                while len(stack) > 0 and stack[-1] < abs(x):
                    stack.pop()
                if len(stack) == 0:
                    ans.append(x)
                else:
                    if stack[-1] == abs(x):
                        stack.pop()
        ans += stack
        return ans
        