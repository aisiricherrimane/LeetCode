class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for w in word:
                count[ord(w) - ord('a')] += 1
            temp[tuple(count)].append(word)
        res = []
        for a in temp.values():
            res.append(a)
        return res

        