# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0
        cur = None 
        
        while l1 or l2 or (carry != 0): 
            if l1 is not None: 
                l1_val_raw = l1.val 
                l1 = l1.next 
            if l2 is not None: 
                l2_val_raw = l2.val 
                l2 = l2.next 

            total_val_raw = l1_val_raw + l2_val_raw + carry
            carry = total_val_raw // 10
            total_val = total_val_raw % 10 

            # handle the nodes. how to get the first one? 
            if cur is None: 
                head = ListNode(total_val)
                cur = head
            else: 
                new = ListNode(total_val)
                cur.next = new 
                cur = cur.next 
            
        
        return head 
            



    