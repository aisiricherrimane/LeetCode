class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        sorted_data = sorted(zip(timestamp, username, website))  # Sort by timestamp automatically
        user_web = defaultdict(list)

        # Step 2: Group websites visited by each user
        for _, user, web in sorted_data:
            user_web[user].append(web)

        # Step 3: Count unique 3-sequence patterns per user
        web_user = defaultdict(int)

        for u, webs in user_web.items():
            unique_combinations = set(combinations(webs, 3))  # Avoid duplicate sequences per user
            for c in unique_combinations:
                web_user[c] += 1
        
        # Step 4: Sort by frequency (descending), then lexicographically
        w = sorted(web_user.keys(), key=lambda x: (-web_user[x], x))
        
        return list(w[0])  # Return the most visited sequence


        