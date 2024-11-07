class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        substrings_freq = defaultdict(int)
        res = [''] * len(arr)

        for string in arr:
            seen = set()
            for length in range(1, len(string) + 1):
                for i in range(len(string) - length + 1):
                    substring = string[i:i+length]
                    if substring not in seen:
                        seen.add(substring)
                        substrings_freq[substring] += 1

        for index, string in enumerate(arr):
            found = False
            for length in range(1, len(string) + 1):
                substrings = []
                for i in range(len(string) - length + 1):
                    s = string[i:i+length]
                    substrings.append(s)
                substrings = sorted(substrings)

                for sub in substrings:
                    if substrings_freq[sub] == 1:
                        res[index] = sub
                        found = True
                        break
                if found:
                    break
        return res
        