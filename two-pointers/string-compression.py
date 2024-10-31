class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        ans = 0
        while i < len(chars):
            letter = chars[i]
            count = 0
            while i < len(chars) and chars[i] == letter:
                i += 1
                count += 1
            chars[ans] = letter
            ans += 1
            if count > 1:
                for n in str(count):
                    chars[ans] = n
                    ans += 1
        return ans
