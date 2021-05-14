"""
Reverse_a_Linked_List.py

vGiven a singly linked list node, return its reverse.

Bonus: Can you do this in \mathcal{O}(1)O(1) space?

Constraints

n ≤ 100,000 where n is the number of nodes in node
Example 1
Input
Visualize
node = [1, 2, 3, 4]
Output
Visualize
[4, 3, 2, 1]
Example 2
Input
Visualize
node = [0, 1]
Output
Visualize
[1, 0]

"""

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):

        prev = None
        current = node

        while current:
            next_node = current.next
            current.next = prev

            prev = current
            current = next_node

        node = prev
        return node
