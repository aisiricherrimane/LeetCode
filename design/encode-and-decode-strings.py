class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        res = ''
        for word in strs:
            res += '#' + str(len(word)) + word
        return res      
        
    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        res = []
        i = 0
        while i < len(s):
            # Find the start of the length prefix
            while s[i] != '#':
                i += 1
            j = i + 1  # Start reading the length
            
            # Find where the length ends
            while j < len(s) and s[j].isdigit():
                j += 1
            
            # Extract the length
            length = int(s[i + 1:j])
            
            # Move to the start of the word and extract it
            i = j
            res.append(s[i:i + length])
            
            # Move past the extracted word
            i += length
        
        return res
