# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, head, pos, val):
        
        # In case linkedlist is empty
        if not head:
            return head
        
        current = head

        # if it is at position 0
        if pos == 0:
            new_element = LLNode(val)
            new_element.next = current
            current = new_element
            
            return new_element

        counter = 0
        while current:
            if counter == pos -1:
                new_element = LLNode(val)
                new_element.next = current.next
                current.next = new_element
                break
            else:
                counter = counter + 1
                current = current.next
        return head
