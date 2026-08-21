# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # reversing the list

        current_r = head 
        prev_r = None 

        while current_r is not None: 
            temp = current_r.next 
            current_r.next = prev_r
            prev_r = current_r
            current_r = temp 

        # oh. just reverse the list and then do it from the "front" lol 

        if prev_r.next is None: 
            return None
        
        
        index = 1
        current = prev_r
        prev = None 

        while index != n: 
            prev = current
            current = current.next 
            index += 1

        # then, current is equal to the nth node. from here, 
        # change the previous node to point to the next node 
        # from current instead of current. get
        # rid of the nth node (turn to none)

        if prev is not None: 
            prev.next = current.next 
        else: 
            prev_r = current.next
        current.next = None 

        # you have to find the head of the new list (the one that was
        # all the way at the BACK of the original one)

        # now all you have to do is reverse it back.. from this point, 
        # the known head for the answer that just needs to be reversed
        # back is prev_r (which will then become the tail, and you need to find the head of.)

        current_f = prev_r
        prev_f = None 

        while current_f is not None: 
            temp = current_f.next
            current_f.next = prev_f
            prev_f = current_f
            current_f = temp

        return prev_f


