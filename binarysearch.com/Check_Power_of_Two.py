"""
Given an integer n greater than or equal to 0, return whether it is a power of two.

Constraints

0 ≤ n < 2 ** 31
Example 1
Input
n = 0
Output
False
Example 2
Input
n = 1
Output
True
Explanation
2^0 = 1

Example 3
Input
n = 2
Output
True
Explanation
2^1 = 2
"""


import math

class Solution:
    def solve(self, n):
        
        # Using maths
        # if 2^x = n then x = log(n) with base 2
        # if x is an integer then return True

        if n == 0:
            return False

        x = math.log(n, 2)
        x_str = str(x)[-2:]
        return x_str == '.0'
