class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_parent = {}  # Union-Find parent map
        email_to_name = {}    # Maps email to the name (person's name)
        
        def find(email):
            if email_to_parent[email] != email:
                email_to_parent[email] = find(email_to_parent[email])
            return email_to_parent[email]
        
        def union(email1, email2):
            root1 = find(email1)
            root2 = find(email2)
            if root1 != root2:
                email_to_parent[root2] = root1
        
        # Step 1: Union all emails of each account
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                email_to_parent.setdefault(email, email)  # Initialize if not present
                email_to_name[email] = name  # Store the name corresponding to this email
                union(first_email, email)   # Union all emails with the first email
        
        # Step 2: Group emails by their root parent
        merged_accounts = {}
        for email in email_to_parent:
            root_email = find(email)  # Find the root email for this email
            if root_email not in merged_accounts:
                merged_accounts[root_email] = []
            merged_accounts[root_email].append(email)
        
        # Step 3: Prepare the result
        result = []
        for root_email, emails in merged_accounts.items():
            result.append([email_to_name[root_email]] + sorted(emails))
        
        return result

        