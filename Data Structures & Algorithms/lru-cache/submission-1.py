class Node:
    def __init__(self, val, key,next = None, prev = None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.dic = {}
        self.dleft = Node(val = -1, key = -1)
        self.dright = Node(val = -1, key = -1)
        self.dleft.next = self.dright
        self.dright.prev = self.dleft
        self.size = 0
    def insert(self, nod):
        pre = self.dright.prev
        pre.next = nod
        nod.next = self.dright
        nod.prev = pre
        self.dright.prev = nod
    
    def rem(self, nod):
        pre = nod.prev
        nex = nod.next
        pre.next = nex
        nex.prev = pre

    def get(self, key: int) -> int:
        if key not in self.dic: return -1
        self.rem(self.dic[key])
        self.insert(self.dic[key])
        return self.dic[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.rem(self.dic[key])
            del self.dic[key]
            self.size-=1
        nod = Node(val = value, key = key)
        self.dic[key] = nod
        self.size+=1
        self.insert(nod)
        if self.size>self.cap:
            self.size-=1
            lru = self.dleft.next
            self.rem(lru)
            del self.dic[lru.key]
        
