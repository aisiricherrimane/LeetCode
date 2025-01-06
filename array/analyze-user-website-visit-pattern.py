class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        data = sorted(zip(timestamp, username, website))
        user_web = defaultdict(list)
        
        for _, user, web in data:
            user_web[user].append(web)
        store = defaultdict(int)
        for user, webs in user_web.items():
            for pattern in set(combinations(webs, 3)):
                store[tuple(pattern)] += 1
        
        res = []
        maxcount = 0
        for pattern, users in store.items():
            if users > maxcount:
                maxcount = users
                res = pattern
        return list(res)

        