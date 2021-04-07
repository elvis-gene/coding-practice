"""
Sum of First N Odd Integers

Given an integer n, return the sum of the first n positive odd integers.

Constraints
n ≤ 1,000

Example 1
Input
n = 5
Output
25
Explanation
The first 5 odd integers are [1, 3, 5, 7, 9] and its sum is 25.
"""

class Solution:
    def solve(self, n):
        
        som = 0
        count = 0
  
        while n > 0:
            count = count + 1 # 2

            if count % 2 != 0:
                som = som + count
                n = n -1
        
        return som
