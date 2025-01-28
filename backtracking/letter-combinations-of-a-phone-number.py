class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'2' : 'abc',
               '3' : 'def',
               '4' : 'ghi',
               '5' : 'jkl',
               '6' : 'mno',
               '7' : 'pqrs',
               '8' : 'tuv',
               '9' : 'wxyz'}
        res = []

        def form(i, curr_str):
            if i == len(digits):
                res.append(curr_str)
                return 

            for c in dic[digits[i]]:
                form(i + 1, curr_str +c)

        if digits: form(0, '')
        return res
