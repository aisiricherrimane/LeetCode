class TimeMap:

    def __init__(self):
        self.store = collections.defaultdict(lambda: defaultdict(str))

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        for t in range(timestamp, -1, -1):
            if t in self.store[key]:
                return str(self.store[key][t])
            else:
                continue
                
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)