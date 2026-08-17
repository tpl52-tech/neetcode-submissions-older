# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # brute force easy: O(n) space. 

        seen = set()

        if head is None:
            return False

        current = head

        while current.next is not None: 

            if current.next in seen: 
                return True
            else: 
                seen.add(current.next)
                current = current.next 
        

        return False 
