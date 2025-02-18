class FileSystem:
    def __init__(self):
        self.path = {}

    def createPath(self, path: str, value: int) -> bool:
        if path == '/' or len(path) == 0 or path in self.path:
            return False
        parent = path[:path.rfind('/')]
        if len(parent) > 1 and parent not in self.path:
            return False
        self.path[path] = value
        return True
        
    
    def get(self, path: str) -> int:
        return self.path.get(path, -1)
    


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)