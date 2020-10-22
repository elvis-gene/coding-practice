"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Notice that you should not modify the linked list.

Follow up:
Can you solve it using O(1) (i.e. constant) memory?

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        # Algorithm:
        # Run through list adding nodes into a list
        # once the next of a node points to a node already existing in the list, we can then
        # say we have a cylce. From there, I will return that node.next
        
        
        # Empty linked list or list of size one
        if not head or not head.next:
            return None
        
        
        nodes = []
        current = head
        
        while current:
            if current not in nodes:
                nodes.append(current)
            else:
                return current
                
            current = current.next
        
        return None
