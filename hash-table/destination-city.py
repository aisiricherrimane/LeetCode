class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        des = set()
        lev = set()
        for path in paths:
            lev.add(path[0])
            des.add(path[1])
        ans = des - lev
        return ans.pop()

        