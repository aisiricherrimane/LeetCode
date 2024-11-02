class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        result = []
        hashmap = defaultdict(list)
        all_substring_frequency = defaultdict(int)
        
        for index in range(len(arr)):
            hashmap[index] = []
            current_substrings = set()

            for i in range(len(arr[index])):
                for j in range(i, len(arr[index])):
                    substring = arr[index][i:j + 1]
                  

                    if substring not in current_substrings:
                        hashmap[index].append(substring)
                        all_substring_frequency[substring] += 1
                        current_substrings.add(substring)
        for key in hashmap:
            result.append('')
            for substrings in sorted(hashmap[key], key = lambda x:(len(x), x)):
                if all_substring_frequency[substrings] == 1:
                    result[key] = substrings
                    break
        return result
        

        '''
        result = []
		hashmap = defaultdict(list)
		all_substrings_frequency = defaultdict(int)

		for index in range(len(arr)):

			hashmap[index] = []
			current_substrings = set()

			for i in range(len(arr[index])):
				for j in range(i, len(arr[index])):

					substring = arr[index][i:j + 1]

					if substring not in current_substrings:

						hashmap[index].append(substring)

						all_substrings_frequency[substring] = all_substrings_frequency[substring] + 1
						current_substrings.add(substring)

		for key in hashmap:

			result.append('')

			for substring in sorted(hashmap[key] , key = lambda x:(len(x), x)):

				if all_substrings_frequency[substring] == 1:

					result[key] = substring
					break

		return result
        '''
