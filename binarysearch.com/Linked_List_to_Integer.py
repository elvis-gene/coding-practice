"""
Linked List to Integer

Given a single linked list node, representing a binary number with most significant digits first, return it as an integer.

Constraints

n ≤ 30 where n the number of nodes in node
Example 1
Input
node = [1, 0, 0]

Output
4

Explanation
The linked list represented 100 in binary
"""


# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        
        if node == None:
            return None

        current = node
        bin_str = str(current.val)

        while current.next:
            current = current.next
            bin_str = bin_str + str(current.val)

        # convert binary to integer
        return int(bin_str, 2)

        
