"""
Interleaved String

Given two strings s0 and s1, return the two strings interleaved, starting with s0. If there are leftover characters in a string they should be added to the end.

Constraints

n ≤ 100,000 where n is the length of s0
m ≤ 100,000 where n is the length of s1
Example 1
Input
s0 = "abc"
s1 = "xyz"
Output
"axbycz"
Example 2
Input
s0 = "abc"
s1 = "x"
Output
"axbc"
"""

class Solution:
    def solve(self, s0, s1):
        
        end = ''
        if len(s0) > len(s1):
            end = s0[len(s1):]
        elif len(s0) < len(s1):
            end = s1[len(s0):]

        output = ''
        for x, y in zip(s0, s1):
            output += x+y
        
        output += end
        return output
