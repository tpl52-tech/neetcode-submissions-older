# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head.next is None:
            return None

        dummy = ListNode()
        dummy.next = head
        
        # make the difference of the two pointers equal to n.

        a = head 
        b = head 

        if head is None: 
            return None

        while b is not None and b.val - a.val != n: 
            b = b.next 


        while b is not None: 
            prev = a
            a = a.next 
            b = b.next
        
        # now, a is the node we want to remove. 

        prev.next = a.next

        return dummy.next
