class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        substrings_frequency = defaultdict(int)

        for string in arr:
            seen_sub_set = set()
            for length in range(1, len(string) + 1):
                for i in range(len(string) - length + 1):
                    substring = string[i:i+length]
                    if substring not in seen_sub_set:
                        substrings_frequency[substring] += 1
                        seen_sub_set.add(substring)
        result = [''] * len(arr)
        for index,string in enumerate(arr):
            found_unique = False
            for length in range(1, len(string) + 1):
                for i in range(len(string) - length + 1):
                    substring = string[i:i+length]
                    if substrings_frequency[substring] == 1:
                        result[index] = substring
                        found = True
                        break
                if found_unique:
                    break
        return result
        
            
