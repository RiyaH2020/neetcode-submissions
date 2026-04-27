# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1=list1
        l2=list2
        dummy=ListNode(0)
        current=dummy
        while(l1 and l2):
            if(l1.val>l2.val):
                current.next=l2
                l2=l2.next
            else:
                current.next=l1
                l1=l1.next
            current=current.next
        current.next=l1 if l1 else l2
        return dummy.next

        