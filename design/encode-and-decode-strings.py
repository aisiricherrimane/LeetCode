class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ''
        for word in strs:
            res += '#' + str(len(word)) + word
        return res      
        
    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = [ ]
        i = 0
        while i < len(s):
            while s[i] != '#':
                i += 1
            j = i + 1
            while j < len(s) and s[j].isdigit():
                j += 1
            i = i + 1
            length = int(s[i:j])

            i = j 
            res.append(s[i:i + length])

            i = i + length
        return res





        

        
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))