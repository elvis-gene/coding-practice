"""
Add Binary Numbers

Given two strings a and b that represent binary numbers, add them and return their sum, also as a string.

The input strings are guaranteed to be non-empty and contain only 1s and 0s.

Constraints

n ≤ 100,000 where n is the length of a
m ≤ 100,000 where m is the length of b
Example 1
Input
a = "1"
b = "1"
Output
"10"
Example 2
Input
a = "111"
b = "1"
Output
"1000"
"""

class Solution:
    def solve(self, a, b):
        
        int_sum = int(a, 2) + int(b, 2)
        return bin(int_sum)[2:]
        # return f'{int_sum:b}'

