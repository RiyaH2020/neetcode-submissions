# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self,head,tail):
        curr=head
        prev=tail
        while(curr!=tail):
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev
        

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        curr=dummy
        while(True):
            group_head=curr.next
            tail=curr
            for _ in range(k):
                tail=tail.next
                if(not tail):
                    return dummy.next
            new_head=self.reverse(group_head,tail.next)
            curr.next=new_head
            curr=group_head



        