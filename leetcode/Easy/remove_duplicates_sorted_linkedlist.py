# Given a sorted linked list, delete all duplicates such that each element appear only once.

# Example 1:

# Input: 1->1->2
# Output: 1->2
# Example 2:

# Input: 1->1->2->3->3
# Output: 1->2->3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        
        return head
