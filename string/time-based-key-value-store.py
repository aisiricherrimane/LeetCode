class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.store:
            self.store[key] = {}
        self.store[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.store:
            return ''
        
        for curr_time in reversed(range(1, timestamp + 1)):
            if curr_time in self.store[key]:
                return self.store[key][curr_time]
        return ''

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)