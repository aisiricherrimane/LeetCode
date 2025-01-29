class Node():
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache():
    def __init__(self, capacity: int):
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

        # cache dict = node
        self.cache = {}
        self.capacity = capacity
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.remove(self.cache[key])
        else:
            self.cache[key] = Node(key,value)

        self.add(self.cache[key])

        if len(self.cache) > self.capacity:
            LRU = self.left.next
            self.remove(LRU)
            del self.cache[LRU.key]
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        else:
            return -1
    
    def remove(self, node):
        p = node.prev
        n = node.next

        p.next, n.prev = n, p

        node.next, node.prev = None, None
    
    def add(self, node):
        p = self.right.prev
        n = self.right

        p.next = node
        n.prev = node
        node.prev = p
        node.next = n


