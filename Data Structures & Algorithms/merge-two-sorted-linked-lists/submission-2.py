# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # strategy : compare list 1 and list 2 elements.
        # if have "next" point towards the smaller element between the 
        # two. if they're equal, just pick the first one's. use "temp"
        # "head", and "next" to navigate through this.

        if list1 == None: 
            return list2
        elif list2 == None: 
            return list1

        current1 = list1 
        current2 = list2

        while current1 != None and current2 != None:                

            if current1.val <= current2.val: 
                temp = current1.next
                current1.next = current2
                current1 = temp
            else: 
                temp = current2.next
                current2.next = current1
                current2 = temp
            

        if list1.val <= list2.val: 
            return list1
        else: 
            return list2