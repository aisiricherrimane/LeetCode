class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i, total, subset):
            if total == target:
                res.append(subset[:])
                return 
            if total > target:
                return
            if i < len(candidates):
                subset.append(candidates[i])
                backtrack(i, total + candidates[i], subset)
                subset.pop()
                backtrack(i + 1, total, subset)

        backtrack(0, 0, [])

        return res
