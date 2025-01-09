class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        N = n
        if len(trust) < N - 1:
            return -1

        indegree = [0] * (N + 1)
        outdegree = [0] * (N + 1)

        for a, b in trust:
            indegree[b] += 1
            outdegree[a] += 1
        
        for i in range(1, N + 1):
            if indegree[i] == N - 1 and outdegree[i] == 0:
                return i
        return -1

        