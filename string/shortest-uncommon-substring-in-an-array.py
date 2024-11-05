from collections import defaultdict
from typing import List

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        substrings_freq = defaultdict(int)

        for string in arr:
            substrings_set = set()
            for l in range(1, len(string) + 1):
                for i in range(len(string) - l + 1):
                    substring = string[i:i + l]
                    if substring not in substrings_set:
                        substrings_freq[substring] += 1
                        substrings_set.add(substring)
        
        res = [''] * len(arr)
        for index, string in enumerate(arr):
            found = False
            for l in range(1, len(string) + 1):
                substrings = []
                for i in range(len(string) - l + 1):
                    substring = string[i:i + l]
                    substrings.append(substring)
                substrings = sorted(substrings)

                for s in substrings:
                    if substrings_freq[s] == 1:
                        res[index] = s
                        found = True
                        break
                if found:
                    break
        return res

            
                

        