class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        substrings_frequency = defaultdict(int)
    
        for string in arr:
            seen_char = set()
            for length in range(1, len(string) + 1):
                
                for i in range(len(string) - length + 1):
                    substring = string[i:i + length]
                    if substring not in seen_char:
                        substrings_frequency[substring] += 1
                        seen_char.add(substring)
        
        result = [""] * len(arr)
        for index, string in enumerate(arr):
            found = False
            substrings = []
            for length in range(1, len(string) + 1):
                
                for i in range(len(string) - length + 1):
                    s = string[i:i + length]
                    if s not in substrings: substrings.append(s)
                substrings = sorted(substrings)
                for c in substrings:
                    if substrings_frequency[c] == 1:
                        result[index] = c
                        found = True
                        break

                if found:
                    break
        return result



      