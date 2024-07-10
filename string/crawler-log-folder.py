class Solution:
    def minOperations(self, logs: List[str]) -> int:
        self.depth = 0
        def helper(i):
            if i > len(logs) - 1:
                return 
            if logs[i] == "../":
                if self.depth > 0:
                    self.depth -= 1
            elif logs[i] == "./":
                pass
            else:
                self.depth  += 1
        
            helper(i + 1)
        helper(0)
        return self.depth
        