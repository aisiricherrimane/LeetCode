"""
# Definition for a Node.
class Node(object):
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        if children is None:
            children = []
        self.val = val
        self.children = children
"""
class WrappableInt:
        def __init__(self, x):
            self.value = x
        def getValue(self):
            return self.value
        def increment(self):
            self.value += 1
class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        serialList = []
        self.s_helper(root, serialList)
        return ''.join(serialList)

    def s_helper(self, root, serialList):
        if not root:
            return 
        serialList.append(chr(root.val + 48))

        for child in root.children:
            self.s_helper(child, serialList)
        serialList.append('#')

	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        
        return self.d_helper(data, WrappableInt(0))

    def d_helper(self, data, index):
        if index.getValue() == len(data):
            return None
        
        node = Node(ord(data[index.getValue()]) - 48, [])
        index.increment()

        while (data[index.getValue()] != '#'):
            node.children.append(self.d_helper(data, index))
        
        index.increment()
        return node