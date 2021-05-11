"""
Given an integer n, return its base 3 representation as a string.

Constraints

0 ≤ n < 2 ** 31
Example 1
Input
n = 7
Output
"21"
Example 2
Input
n = 11
Output
"102"
"""

class Solution:
    def solve(self, n):

        if n == 0:
            return "0"
        
        output = list()

        while n > 0:
            output.append(str(n % 3))
            n = n//3

        output.reverse()
        return ''.join(output)
