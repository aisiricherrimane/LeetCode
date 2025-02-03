class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        user_web = defaultdict(list)
        for i, user in enumerate(username):
            user_web[user].append(website[i])

        web_user = defaultdict(int)

        for u, webs in user_web.items():
            for c in combinations(webs, 3):
                web_user[c] += 1
        
        w = sorted(web_user.keys(), key= lambda x:(-web_user[x], x))
        return list(w)[0]

        