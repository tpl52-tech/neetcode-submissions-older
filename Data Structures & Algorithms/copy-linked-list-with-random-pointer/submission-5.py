"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # make a hash map old : new after making the first pass new 
        # linked list. 

        # create the new linked list 

        if head is None:
            return None

        

        dummy = Node(1)
        dummy.next = head

        a = dummy 
        b = head 

        old_to_new = {}

        while b: 
            a.next = Node(b.val)
            old_to_new[b] = a.next
            a = a.next 
            b = b.next 
        
        # ohh shit the old value of the random will be connected 
        # to its own new value through the hashmap 

        c = head 

        while c: 
            if c.random is None: 
                old_to_new[c].random = None 
            else: 
                old_to_new[c].random = old_to_new[c.random]
            c = c.next 
        
        return dummy.next

            