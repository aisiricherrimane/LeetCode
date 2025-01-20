class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        data = sorted(zip(timestamp, username, website))
        user_web = defaultdict(list)

        for _, user, web in data:
            user_web[user].append(web)
        
        web_count = defaultdict(int)
        for user, web in user_web.items():
            for pattern in set(combinations(web, 3)):
               web_count[pattern] += 1
        
        most_visited = sorted(web_count.keys(), key = lambda x:(-web_count[x], x))

        return list(most_visited[0])
         

            
        