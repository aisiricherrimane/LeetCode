class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        # Split the pattern into prefix and suffix
        temp = p.split('*')
        pre = temp[0]
        suf = temp[1]
        
        i = 0
        while i <= len(s) - len(pre):  # Ensure `pre` fits into the substring
            # Check if `pre` matches the current substring
            if pre == s[i:i+len(pre)]:
                # Check if `suf` is in the remaining substring after `pre`
                if suf == "" or s[i+len(pre):].startswith(suf):
                    return True
            i += 1  # Increment `i` to avoid infinite loop
        return False