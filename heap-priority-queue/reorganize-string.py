class Solution:
    def reorganizeString(self, s: str) -> str:
        char_count = Counter(s)
        max_count = 0
        letter = ''

        for c, f in char_count.items():
            if f > max_count:
                max_count = f
                letter = c
        ind = 0
        res = [''] * len(s)

        if max_count > (len(s) + 1) // 2:
            return ''
        
        while char_count[letter] != 0:
            res[ind] = letter
            ind += 2
            char_count[letter] -= 1
            
        if ind >= len(res):
                    ind = 1
        for char, count in char_count.items():
            while count > 0:
                res[ind] = char
                count -= 1
                ind += 2
        return ''.join(res)

        