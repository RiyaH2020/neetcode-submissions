# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        N=0
        while(curr):
            N+=1
            curr=curr.next
        index=N-n
        if(index==0):
            head=head.next
            return head
        curr=head
        for i in range(index-1):
            curr=curr.next
        curr.next=curr.next.next
        return head

        