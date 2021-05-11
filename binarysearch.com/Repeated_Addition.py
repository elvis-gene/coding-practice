"""
Given a positive integer n, sum all of its digits to get a new number. Repeat this operation until the new number is less than 10 and return it.

Constraints

1 ≤ n < 2 ** 31
Example 1
Input
n = 8835
Output
6
Explanation
8 + 8 + 3 + 5 = 24
2 + 4 = 6
"""

class Solution:
    def solve(self, n):
        
        som = n

        while som > 9 and som < 2**31:
            som = self.add(som)
        return som

    def add(self, num):
        som = 0

        while num > 0:
            suff = num%10
            som = som + suff
            num = num//10
        return som
