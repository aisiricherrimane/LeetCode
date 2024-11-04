class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        map_ind_to_sub = defaultdict(list)
        substring_freq = defaultdict(int)
        
        for index in range(len(arr)):
            sub_set = set()
            for i in range(len(arr[index])):
                for j in range(i, len(arr[index])):
                    s = arr[index][i:j+1]
                    if s not in sub_set:
                        map_ind_to_sub[index].append(s)
                        substring_freq[s] += 1
                        sub_set.add(s)
        res = []
        for index in map_ind_to_sub:
            res.append('')
            for s in sorted(map_ind_to_sub[index], key=lambda x:(len(x), x)):
                if substring_freq[s] == 1:
                    res[index] = s
                    break
        return res