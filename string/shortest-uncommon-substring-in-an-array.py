def shortestSubstrings(self, arr: List[str]) -> List[str]:
        def is_unique(substring, current_index):
        # Check if the substring appears in any other string
            for i, other_string in enumerate(arr):
                if i != current_index and substring in other_string:
                    return False
            return True

        answer = []  # To store the result for each string in arr

        # Process each string in arr
        for index, string in enumerate(arr):
            found_unique = False
            min_unique_substring = ""  # To track the lexicographically smallest unique substring

            # Try substrings of increasing lengths
            for length in range(1, len(string) + 1):
                substrings = sorted(set(string[i:i+length] for i in range(len(string) - length + 1)))
                
                for substring in substrings:
                    # Check if this substring is unique
                    if is_unique(substring, index):
                        # Update if it's the first found or lexicographically smaller
                        min_unique_substring = substring
                        found_unique = True
                        break

                if found_unique:
                    break

            # Append the shortest unique substring or empty string if none found
            answer.append(min_unique_substring if found_unique else "")
        
        return answer