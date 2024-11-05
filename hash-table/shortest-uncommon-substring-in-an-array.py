class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        def is_unique(substring, index):
            for i, sub_func_string in enumerate(arr):
                if i != index and substring in sub_func_string:
                    return False
            return True
        answer = []
        for index, string in enumerate(arr):
            found_unique = False
            min_unique_substring = ""

            for length in range(1, len(string) + 1):
                unique_substrings = set()
                for i in range(len(string) - length + 1):
                    substring = string[i:i+length]
                    unique_substrings.add(substring)
                substrings = sorted(unique_substrings)
                
                for substring in substrings:
                    if is_unique(substring, index):
                        min_unique_substring = substring
                        found_unique = True
                        break
                
                if found_unique:
                    break
        

            answer.append(min_unique_substring if found_unique else '')

        return answer
  
