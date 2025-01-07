class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        unique_palindromes = set()

        # Iterate over all lowercase English letters (from 'a' to 'z')
        for char in set(s):
            # Find the first and last occurrence of the current character
            first = s.find(char)
            last = s.rfind(char)
            
            # If there's a valid range to form a palindrome
            if last - first > 1:
                # Add all unique characters between the first and last occurrence
                for middle_char in set(s[first + 1:last]):
                    unique_palindromes.add(char + middle_char + char)
        
        # Return the number of unique palindromic subsequences
        return len(unique_palindromes)