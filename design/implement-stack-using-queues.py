class MyStack:

    def __init__(self):
        self.queue = deque()
        
    def push(self, x: int) -> None:
        self.queue.append(x)
        
    def pop(self) -> int:
        for i in range(len(self.queue) - 1):
            self.push(self.queue.popleft())
        return self.queue.popleft()

        

    def top(self) -> int:
        n = len(self.queue)
        return self.queue[n - 1]
    def empty(self) -> bool:
        if not self.queue:
            return False

        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()