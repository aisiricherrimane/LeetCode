from collections import defaultdict
from itertools import combinations

class Solution:
    def mostVisitedPattern(self, username, timestamp, website):
        data = sorted(zip(timestamp, username, website))
        
        user_web = defaultdict(list)
        for _, user, web in data:
            user_web[user].append(web)
        
        store = defaultdict(set)
        for user, webs in user_web.items():
            for pattern in set(combinations(webs, 3)):
                store[pattern].add(user)
        
        maxcount, res = 0, []
        for pattern, users in store.items():
            if len(users) > maxcount or (len(users) == maxcount and pattern < tuple(res)):
                maxcount = len(users)
                res = pattern
        
        return list(res)
