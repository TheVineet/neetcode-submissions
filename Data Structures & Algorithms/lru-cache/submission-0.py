class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} #Hash Map, key to node
        self.left = Node(0,0) #Dummy left node
        self.right = Node(0,0) #Dummy right node
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self,node : Node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
    
    def insert(self, node : Node, next : node):
        prev = next.prev
        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache.get(key)
        val = node.value
        
        # remove the current node
        self.remove(node)

        # insert the current node to the end
        self.insert(node, self.right)

        # return the val
        return val
    

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache.get(key))
            del self.cache[key]

        count = len(self.cache)

        if count == self.capacity:
            # Remove the first
            first = self.left.next
            self.remove(first)
            del self.cache[first.key]
        node = Node(key,value)
        self.cache[key] = node
        self.insert(node, self.right)

        return None
        
        
        
