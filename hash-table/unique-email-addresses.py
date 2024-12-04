class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
    
        for email in emails:
            local, domain = email.split('@')  # Split into local and domain parts
            # Process the local name: remove '.' and ignore everything after '+'
            local = local.split('+')[0].replace('.', '')
            # Combine the processed local name with the domain
            unique_emails.add(local + '@' + domain)
        
        return len(unique_emails)

        