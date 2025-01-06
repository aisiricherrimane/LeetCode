class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        data = sorted(zip(timestamp, username, website))
        user_web = defaultdict(list)
        
        for _, user, web in data:
            user_web[user].append(web)

        store = defaultdict(set)

        for user, webs in user_web.items():
            for pattern in set(combinations(webs, 3)):
                store[pattern].add(user)
        
        res = []
        maxcount = 0
        for pattern, users in store.items():
            if len(users) > maxcount or (len(users) == maxcount and list(pattern) < res):
                maxcount = len(users)
                res = list(pattern)
        return res

        