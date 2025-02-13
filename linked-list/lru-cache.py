class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def put(self, key, value):
        if key in self.cache:
            self.cache[key].val = value
            self.remove(self.cache[key])
        else:
            self.cache[key] = Node(key, value)

        self.add(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            del self.cache[lru.key]
            self.remove(lru)
    
    def get(self, key):
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.add(self.cache[key])
        return self.cache[key].val
    
    def add(self, node):
        p = self.right.prev
        n = self.right

        p.next = node
        n.prev = node
        node.prev = p
        node.next = n
    
    def remove(self, node):
        p = node.prev
        n = node.next

        p.next = n
        n.prev = p


