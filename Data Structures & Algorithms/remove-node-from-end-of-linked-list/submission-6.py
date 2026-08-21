# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # reversing the list

        # oh. just reverse the list and then do it from the "front" lol 

        if head.next is None: 
            return None
        
        index = 1
        current = head
        prev = None 

        while index != n: 
            prev = current
            current = current.next 
            index += 1

        # then, current is equal to the nth node. from here, 
        # change the previous node to point to the next node 
        # from current instead of current. get
        # rid of the nth node (turn to none)

        prev.next = current.next 
        current.next = None 

        return head 


