class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.cache = {}
        self.left.next, self.right.prev = self.right, self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add_node(self.cache[key])
            return self.cache[key].value
        else:
            return -1
    
    def add_node(self, node):
        p = self.right.prev
        n = self.right
        node.prev, node.next = p, n
        p.next, n.prev = node, node

    def remove(self, node):
        p = node.prev
        n = node.next
        p.next, n.prev = n, p

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value
            self.remove(self.cache[key])
        else:
            self.cache[key] = Node(key, value)
        self.add_node(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(self.left.next)
            del self.cache[lru.key]
        


      

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)