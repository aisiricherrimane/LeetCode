from collections import defaultdict
from typing import List

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        # Dictionary to store the frequency of each substring across all strings
        substring_freq = defaultdict(int)
        
        # Step 1: Count all possible substrings across all strings up to a reasonable length
        for word in arr:
            seen_substrings = set()
            for length in range(1, len(word) + 1):  # Increase substring length gradually
                for i in range(len(word) - length + 1):
                    substring = word[i:i + length]
                    if substring not in seen_substrings:
                        substring_freq[substring] += 1
                        seen_substrings.add(substring)
        
        # Step 2: Find the shortest unique substring for each word
        result = []
        for word in arr:
            found = False
            for length in range(1, len(word) + 1):  # Start with shortest substrings
                for i in range(len(word) - length + 1):
                    substring = word[i:i + length]
                    # Check if this substring is unique across all strings
                    if substring_freq[substring] == 1:
                        result.append(substring)
                        found = True
                        break
                if found:
                    break  # Stop once we find the shortest unique substring for this word

            # If no unique substring is found, append an empty string
            if not found:
                result.append("")
        
        return result
