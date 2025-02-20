class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        prefix = []
        plate = 0
        for i in range(len(s)):
            if s[i] == '*':
                plate += 1
            prefix.append(plate)

        left_candle = [-1] * len(s)
        closet = -1
        for i in range(len(s)):
            if s[i] == '|':
                closet = i
            left_candle[i] = closet
        
        right_candle = [-1] * len(s)
        closet = -1
        for i in range(len(s) -1, -1, -1):
            if s[i] == '|':
                closet = i
            right_candle[i] = closet
        
        res = []

        for l,  r in queries:
            left_bound = right_candle[l]
            right_bound = left_candle[r]

            if left_bound != -1 and right_bound != -1 and left_bound < right_bound:
                res.append(prefix[right_bound] - prefix[left_bound])
            else:
                res.append(0)
              
        return res
        


        