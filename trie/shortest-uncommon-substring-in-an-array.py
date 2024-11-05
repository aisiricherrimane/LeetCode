from collections import defaultdict
from typing import List

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        result = []
        hashmap = defaultdict(list)
        substring_freq = defaultdict(int)

        for index in range(len(arr)):
            substrings = set()
            for i in range(len(arr[index])):
                for j in range(i, len(arr[index])):
                    subs = arr[index][i:j + 1]
                    
                    if subs not in substrings:
                        hashmap[index].append(subs)
                        substring_freq[subs] += 1
                        substrings.add(subs)
        
        for key in hashmap:
            result.append('')
            for s in sorted(hashmap[key], key = lambda x:(len(x), x)):
                if substring_freq[s] == 1:
                    result[key] = s
                    break
        return result

            
                

        