class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, temp, tot):
            if tot > target:
                return 
            if tot == target:
                res.append(temp[:])
                return
            if i >= len(candidates):
                return
            temp.append(candidates[i])
            dfs(i, temp, tot + candidates[i])

            temp.pop()
            dfs(i + 1, temp, tot)
        dfs(0, [], 0)
        return res
        