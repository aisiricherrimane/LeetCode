class MinStack():
    def __init__(self):
        self.stack = []
        self.minStack = []
    
    def push(self, val):
        if not self.stack:
            self.stack.append(val)
            self.minStack.append(val)
        v = self.minStack[-1]
        self.minStack.append(v) if v < val else self.minStack.append(val)
        self.stack.append(val)

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.minStack.pop()
    
    def getMin(self):
        return self.minStack[-1]
    
    def top(self):
        return self.stack[-1]
        



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()