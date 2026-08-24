# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head 

        if head.next is None: 
            return None

        counter = head
        length = 0

        while counter is not None: 
            counter = counter.next 
            length += 1

        # get the node right before the one we want to remove 

        a = dummy.next
        
        for i in range (length - n - 1): 
            a = a.next 
        
        a.next = a.next.next 

        return dummy.next 


