"""
Balanced Brackets Sequel

Given a string s containing round, curly, and square open and closing brackets, return whether the brackets are balanced.

Constraints

n ≤ 100,000 where n is the length of s
Example 1
Input
s = "[(])"
Output
False
Example 2
Input
s = "([])[]({})"
Output
True
"""

class Solution:
    def solve(self, s):
        
        pairs = {']':'[', '}':'{', ')':'('}
        stack = []

        for bracket in s:
            if stack and stack[-1] == pairs.get(bracket):
                stack.pop()
            else:
                stack.append(bracket)
        
        return not stack
