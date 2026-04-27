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
        curr=head
        while(curr):
            curr_copy=Node(curr.val)
            curr_copy.next=curr.next
            curr.next=curr_copy
            curr=curr_copy.next
        curr=head
        while(curr):
            if(curr.random):
                curr.next.random=curr.random.next
            curr=curr.next.next
        curr=head
        head2=head.next if head else None
        while(curr):
            copy=curr.next
            curr.next=copy.next
            copy.next=copy.next.next if copy.next else None
            curr=curr.next
        return head2