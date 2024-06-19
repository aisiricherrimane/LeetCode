class Solution:
    def reverseWords(self, s: str) -> str:
    # Step 1: Split the string by whitespace to get the words
        words = s.split()
        
        # Step 2: Reverse the list of words
        reversed_words = words[::-1]
        
        # Step 3: Join the reversed words with a single space
        reversed_string = ' '.join(reversed_words)
        
        return reversed_string
    
        
        