class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        res = []
        prefix_plate = [0] * n
        plates = 0

        for i in range(n):
            if s[i] == '*':
                plates += 1
            prefix_plate[i] = plates
        
        left_candle = [-1] * n
        nearest = -1
        for i in range(n):
            if s[i] == '|':
                nearest = i
            left_candle[i] = nearest
        
        right_candle = [-1] * n
        nearest = -1
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                nearest = i
            right_candle[i] = nearest
        
        for start, end in queries:
            left_bound = right_candle[start]
            right_bound = left_candle[end]

            if left_bound != -1 and right_bound != -1 and left_bound < right_bound:
                res.append(prefix_plate[right_bound] - prefix_plate[left_bound])
            else:
                res.append(0)
        return res

        