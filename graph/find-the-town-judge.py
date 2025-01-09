class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        judge = trust[0][1]

        for common, maybe in trust:
            if maybe != judge:
                return -1
        return judge
            
        