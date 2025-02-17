class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        data = sorted(zip(timestamp, username, website))
        user_website = defaultdict(list)

        for _, u, w in data:
            user_website[u].append(w)
        
        websites_count = defaultdict(int)
        for u, w in user_website.items():
            for s in set(combinations(w, 3)):
                websites_count[s] += 1
        
        result = sorted(websites_count.keys(), key = lambda x:( -websites_count[x], x))

        return list(result[0])


        