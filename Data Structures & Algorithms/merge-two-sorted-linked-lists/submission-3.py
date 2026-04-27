# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        curr=dummy
        p1=list1
        p2=list2
        while(p1 or p2):
            if(p1 and p2 and p1.val<=p2.val):
                curr.next=p1
                curr=curr.next
                p1=p1.next
            elif(p1 and p2 and p2.val<p1.val):
                curr.next=p2
                curr=curr.next
                p2=p2.next
            elif(p1==None):
                curr.next=p2
                curr=curr.next
                p2=p2.next
            elif(p2==None):
                curr.next=p1
                curr=curr.next
                p1=p1.next
        return dummy.next
            
                
                

        