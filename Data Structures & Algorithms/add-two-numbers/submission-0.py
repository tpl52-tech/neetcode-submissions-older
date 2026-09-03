# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # strategy: . Then, reverse the digits by turning 
        # the int into a string and iterating through it .
        # from here, iterate through it once more to make the 
        # linked list in this reversed order and we have our answer. 

        current_power_of_ten_l1 = 0
        l1_value = 0

        while l1: 
            l1_value += l1.val * (10 ** current_power_of_ten_l1)
            current_power_of_ten_l1 += 1
            l1 = l1.next 

        current_power_of_ten_l2 = 0
        l2_value = 0

        while l2: 
            l2_value += l2.val * (10 ** current_power_of_ten_l2)
            current_power_of_ten_l2 += 1
            l2 = l2.next 

        result_value = l1_value + l2_value 

        result_value_string = str(result_value)

        dummy = None

        head = ListNode(result_value_string[int(len(result_value_string) - 1)])
        a = head

        if len(result_value_string) == 1: 
            return a 

        for i in range (len(result_value_string) - 2, -1, -1): 
            new = ListNode(int(result_value_string[i]))
            a.next = new 
            a = a.next 

        return head
        

        