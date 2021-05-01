"""
Kth Last Node of a Linked List

Given a singly linked list node, return the value of the kth last node (0-indexed). k is guaranteed not to be larger than the size of the linked list.

This should be done in O(1) space.

Constraints
n ≤ 100,000 where n is the length of node

Example 1
Input
Visualize
node = [1, 2]
k = 1
Output
1
Explanation
The second last node has the val of 1

Example 2
Input
Visualize
node = [0, 1, 2, 3]
k = 2
Output
1
"""


# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node, k):
        
        # Count the number of items in the array
        # Iterate the array and compare if the index of the current element (starting at index 1) plus k equals the size of
        # the list.
        # Example: list = [1, 2]. size = 2.

        current = node
        size = 0
        while current:
            size += 1
            current = current.next
        
        if k > size:
            return None

        current = node
        index = 0
        while current:
            index += 1

            if index + k == size:
                return current.val
            current = current.next
