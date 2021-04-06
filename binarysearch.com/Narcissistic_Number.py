"""
Narcissistic Number

Given an integer n, return whether it is equal to the sum of its own digits raised to the power of the number of digits.

Example 1
Input
n = 153
Output
True
Explanation
153 = 1 ** 3 + 5 ** 3 + 3 ** 3
"""

class Solution:
    def solve(self, n):
        
        # Algorithm
        # Without converting to a string.

        target = n
        num_digits = len(str(n))
        
        som = 0
        while n > 0:
            # Get last digit of the number
            suf = n % 10    
            # Update number after removing the last digit
            n = n//10

            som += suf**num_digits
        
        return som == target
