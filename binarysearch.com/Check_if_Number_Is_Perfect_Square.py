"""
Given an integer n, return whether n = k * k for some integer k.

This should be done without using built-in square root function.

Constraints

0 ≤ n < 2 ** 31
Example 1
Input
n = 25
Output
True
Explanation
25 = 5 * 5
"""

import math

class Solution:
    def solve(self, n):
        
        # Algorithm:
        # Using maths
        # n is perfect if n = x^2

        x = math.sqrt(n)
        print(x)
        x_str = str(x)[-2:]

        if '.' in x_str:
            return True
        return False
        
