class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        data = sorted(zip(timestamp, username, website))

        user_web = defaultdict(list)
        for t, u, w in data:
            user_web[u].append(w)

        web_user_count = defaultdict(int)
        for u, w in user_web.items():
            for c in combinations(w, 3):
                web_user_count[c] += 1
        
        res = sorted(web_user_count.keys(), key = lambda x:(-web_user_count[x], x))

        return list(res[0])
        
       