from typing import List

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        unique_substrings = set()
        non_unique_substrings = set()
        result = [""] * len(arr)

        # First pass: Identify unique substrings
        for string in arr:
            for length in range(1, len(string) + 1):
                found = False
                for i in range(len(string) - length + 1):
                    substring = string[i:i + length]
                    if substring in non_unique_substrings:
                        continue
                    if substring in unique_substrings:
                        # If seen more than once, move to non-unique
                        unique_substrings.remove(substring)
                        non_unique_substrings.add(substring)
                    else:
                        unique_substrings.add(substring)
                        result[arr.index(string)] = substring
                        found = True
                        break
                if found:
                    break

        return result
