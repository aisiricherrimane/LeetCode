class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        visit = set()
        temp = trust[0][1]

        for p, maybej in trust:
            if temp != maybej:
                return -1
        return temp
