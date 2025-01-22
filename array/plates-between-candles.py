from typing import List

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        
        # Prefix sum for plates
        prefix_plates = [0] * n
        plates = 0
        for i in range(n):
            if s[i] == '*':
                plates += 1
            prefix_plates[i] = plates
        
        # Nearest left and right candles
        left_candle = [-1] * n
        right_candle = [-1] * n
        
        # Fill nearest left candle
        nearest = -1
        for i in range(n):
            if s[i] == '|':
                nearest = i
            left_candle[i] = nearest
        
        # Fill nearest right candle
        nearest = -1
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                nearest = i
            right_candle[i] = nearest
        
        # Process queries
        result = []
        for left, right in queries:
            left_bound = right_candle[left]
            right_bound = left_candle[right]
            
            if left_bound != -1 and right_bound != -1 and left_bound < right_bound:
                result.append(prefix_plates[right_bound] - prefix_plates[left_bound])
            else:
                result.append(0)
        
        return result
