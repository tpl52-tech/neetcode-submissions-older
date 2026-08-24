# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head 

        a = dummy  
        b = dummy
        
        for i in range (n) :
            b = b.next 
        
        while b.next : 
            b = b.next 
            a = a.next 
        
        a.next = a.next.next 

        return dummy.next 