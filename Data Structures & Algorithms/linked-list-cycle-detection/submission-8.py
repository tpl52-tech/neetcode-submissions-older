# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        tracker = head
        slow = head 
        fast = head 
        

        while tracker and slow and fast and fast.next is not None: 
            slow = slow.next
            fast = fast.next.next

            if fast == slow: 
                return True

            tracker = tracker.next
        
        return False 

        
