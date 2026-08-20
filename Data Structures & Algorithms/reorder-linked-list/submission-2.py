# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
    
        # find the middle of the linked list 
        slow = head
        fast = head

        while fast.next and fast.next.next is not None: 
            slow = slow.next 
            fast = fast.next.next
        
        # reverse the second half 
        second = second_original = slow.next 
        slow.next = prev = None 

        while second:
            temp = second.next
            second.next = prev
            prev = second 
            second = temp 
        
        # merge the two 
        slow_list = head 
        reversed_list = prev

        # put inside of some sort of loop 
        while slow_list is not None and reversed_list is not None: 
            temp_slow = slow_list.next 
            slow_list.next = reversed_list
            slow_list = temp_slow 
            temp_rev = reversed_list.next
            reversed_list.next = slow_list 
            reversed_list = temp_rev 

        

