import collections

class TimeMap:

    def __init__(self):
        self.store = collections.defaultdict(lambda: defaultdict(str))

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Only set if the timestamp is not already in the dictionary
        if self.store[key][timestamp] == "":
            self.store[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        # Start from the given timestamp and go backward to find the nearest one
        for t in range(timestamp, -1, -1):
            if t in self.store[key]:
                return self.store[key][t]
        return ""
