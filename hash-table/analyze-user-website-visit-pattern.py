class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        user_web = defaultdict(list)
        for i, user in enumerate(username):
            user_web[user].append(website[i])
        store = defaultdict(int)
        for user, webs in user_web.items():
            store[tuple(webs)] += 1
        maxcount = 0
        res = []
        for key, count in sorted(store.items(), key=lambda x: x[0]):
            if count > maxcount:
                maxcount = count
                res = list(key)
        return res