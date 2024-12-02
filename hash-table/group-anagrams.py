class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = collections.defaultdict(list)
        for word in strs:
            count = [0] * 26
            for w in word:
                count[ord(w) - ord('a')] = 1 + count[ord(w) - ord('a')]
            temp[tuple(count)].append(word)
        
        return list(temp.values())
