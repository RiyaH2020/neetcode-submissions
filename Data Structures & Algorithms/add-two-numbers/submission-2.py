# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        curr=dummy
        c=0
        while(l1 or l2 ):
            if(l1 and l2 and l1.val+l2.val+c<=9):
                curr.next=ListNode(l1.val+l2.val+c)
                l1=l1.next
                l2=l2.next
                c=0
                curr=curr.next
            elif(l1 and l2):
                curr.next=ListNode((l1.val+l2.val+c)%10)
                c=1
                l1=l1.next
                l2=l2.next
                curr=curr.next
            elif(l1):
                if(l1.val+c<=9):
                    curr.next=ListNode(l1.val+c)
                    c=0
                    l1=l1.next
                    curr=curr.next
                else:
                    curr.next=ListNode((l1.val+c)%10)
                    c=1
                    l1=l1.next
                    curr=curr.next
            elif(l2):
                if(l2.val+c<=9):
                    curr.next=ListNode(l2.val+c)
                    c=0
                    l2=l2.next
                    curr=curr.next
                else:
                    curr.next=ListNode((l2.val+c)%10)
                    c=1
                    l2=l2.next
                    curr=curr.next
        if(c==1):
            curr.next=ListNode(1)
        return dummy.next
                    
                



            
