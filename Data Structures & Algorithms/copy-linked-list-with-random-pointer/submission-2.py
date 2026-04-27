"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr=head
        hashMap={}
        while(curr):
            hashMap[curr]=Node(curr.val)
            curr=curr.next
        curr=head
        
        new=hashMap[curr]
        while(curr):
            if(curr.next):
                hashMap[curr].next=hashMap[curr.next]
            else:
                hashMap[curr].next=None
            if(curr.random):
                hashMap[curr].random=hashMap[curr.random]
            else:
                hashMap[curr].random=None
            curr=curr.next
        return new if head else  None
            



        