import collections

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp, value])
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        for t, v in reversed(self.store[key]):
            if t <= timestamp:
                return v
        return ''
        
        