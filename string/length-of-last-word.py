class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split(' ')
        print(arr)
        for i in range(len(arr) - 1, -1, -1):
            if arr[i]== '':
                continue
            else:
                return len(arr[i])
        

            

        