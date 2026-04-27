# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cal=head
        len1=0
        while(cal):
            len1=len1+1
            cal=cal.next
        n1=len1-n
        print(n1)
        if(n1==0):
            return head.next
        temp=head
        i=0
        while(temp):
            if(i==n1-1):
                temp.next=temp.next.next
            i=i+1
            temp=temp.next
        return head


        

        