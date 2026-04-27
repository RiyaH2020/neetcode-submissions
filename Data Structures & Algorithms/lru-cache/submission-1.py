class Node:
    def __init__(self,key,value):
        self.key=key
        self.val=value
        self.prev=None
        self.next=None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head
    
    def _remove(self,node):
        prv,nxt=node.prev,node.next
        prv.next=nxt
        nxt.prev=prv
    
    def _add_to_front(self,node):
        node.next=self.head.next
        node.prev=self.head
        self.head.next.prev=node
        self.head.next=node

        


    def get(self, key: int) -> int:
        if(key in self.cache):
            self._remove(self.cache[key])
            self._add_to_front(self.cache[key])
            return self.cache[key].val
        else:
            return -1
        
        

        

    def put(self, key: int, value: int) -> None:
        if(key in self.cache):
            self.cache[key].val=value
            self._remove(self.cache[key])
            self._add_to_front(self.cache[key])
        else:
            self.cache[key]=Node(key,value)
            self._add_to_front(self.cache[key])
            
        if(len(self.cache)>self.capacity):
            node=self.tail.prev
            self._remove(node)
            del self.cache[node.key]




        
