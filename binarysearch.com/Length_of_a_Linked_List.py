"""
Length of a Linked List

Given a singly linked list node, return its length. The linked list has fields next and val.

Constraints
n ≤ 100,000 where n is the number of nodes in node

Example 1
Input
Visualize
node = [5, 4, 3]

Output
3

Explanation
This linked list has 3 nodes.

Example 2
Input
Visualize
node = [1, 2]

Output
2
Explanation
This linked list has 2 nodes.
"""

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        
        if node == None:
            return 0
            
        count = 1
        current = node

        while current.next:
            current = current.next
            count = count + 1
        
        return count
        
