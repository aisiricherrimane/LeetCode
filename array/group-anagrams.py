class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = collections.defaultdict(list)

        for word in strs:
            count = [0] * 26
            for w in word:
                count[ord('a') - ord(w)] += 1
            temp[tuple(count)].append(word)
        res = []
        for t in temp.values():
            res.append(t)
        return res
