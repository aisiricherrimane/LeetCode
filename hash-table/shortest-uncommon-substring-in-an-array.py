class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        hashmap = defaultdict(list)
        substring_freq = defaultdict(int)

        for index in range(len(arr)):
            subs = set()
            for i in range(len(arr[index])):
                for j in range(i, len(arr[index])):
                    temp = arr[index][i: j + 1]
                    if temp not in subs:
                        hashmap[index].append(temp)
                        substring_freq[temp] += 1
                        subs.add(temp)
        res = []
        for index in hashmap.keys():
            res.append('')
            for substring in sorted(hashmap[index], key = lambda x:(len(x), x)):
                if substring_freq[substring] == 1:
                    res[index] = substring
                    break
        return res




        