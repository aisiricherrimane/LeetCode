from collections import defaultdict
from typing import List

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        # Step 1: Count the frequency of each substring across all strings
        substring_freq = defaultdict(int)
        
        for word in arr:
            seen_substrings = set()  # Track substrings seen in this word to avoid counting duplicates
            for length in range(1, len(word) + 1):  # Loop over substring lengths
                for i in range(len(word) - length + 1):
                    substring = word[i:i + length]
                    if substring not in seen_substrings:
                        substring_freq[substring] += 1
                        seen_substrings.add(substring)
        
        # Step 2: Find the shortest lexicographically smallest unique substring for each word
        result = []
        for word in arr:
            found = False
            for length in range(1, len(word) + 1):  # Start from shortest substrings
                # Generate all substrings of the current length and sort them lexicographically
                substrings = sorted(word[i:i + length] for i in range(len(word) - length + 1))
                
                for substring in substrings:
                    # Check if this substring is unique (appears only once across all words)
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

