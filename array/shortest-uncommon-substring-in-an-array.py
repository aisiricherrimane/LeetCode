class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        substring_freq = defaultdict(int)
        
        for string in arr:
            for length in range(1, len(string) + 1):
                substring_seen = set()
                for i in range(len(string) - length + 1):
                    substring = string[i:i+length]
                    if substring not in substring_seen:
                        substring_freq[substring] += 1
                        substring_seen.add(substring)
        
        res = [''] * len(arr)

        for index, string in enumerate(arr):
            found = False
            for length in range(1, len(string) + 1):
                substring_seen = []
                for i in range(len(string) - length + 1):
                    substring = string[i:i+length]
                    substring_seen.append(substring)
                
                substring_seen = sorted(substring_seen)
                for s in substring_seen:
                    if substring_freq[s] == 1:
                        res[index] = s
                        found = True
                        break
                if found:
                    break
        return res
                    

        