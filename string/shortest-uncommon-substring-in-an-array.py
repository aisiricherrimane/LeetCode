class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        substring_freq = defaultdict(int)
        res = [None] * len(arr)  # Result array to store unique substrings
        
        # Calculate global frequency of each substring by increasing lengths
        for length in range(1, max(len(s) for s in arr) + 1):
            # Track frequencies at this substring length
            current_length_freq = defaultdict(int)
            
            # Generate substrings of the current length
            for index, s in enumerate(arr):
                if res[index] is not None:  # Skip if we've already found a unique substring
                    continue
                for i in range(len(s) - length + 1):
                    sub = s[i:i + length]
                    current_length_freq[sub] += 1
            
            # Update global frequency and find unique substrings
            for index, s in enumerate(arr):
                if res[index] is not None:  # Skip if already found
                    continue
                for i in range(len(s) - length + 1):
                    sub = s[i:i + length]
                    # Check if substring is unique
                    if current_length_freq[sub] == 1:
                        res[index] = sub
                        break
        
        return res
