# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1=list1
        p2=list2
        list3=[]
        while(p1):
            list3.append(p1.val)
            p1=p1.next
        while(p2):
            list3.append(p2.val)
            p2=p2.next
        list3.sort()
        dummy = ListNode(0)   # fake head
        curr = dummy
        for val in list3:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next


        