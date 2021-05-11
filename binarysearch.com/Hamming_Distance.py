"""
Given two integers x, and y return the number of positions where their values differ in their binary representations as a 32-bit integer.

Constraints

0 ≤ x, y < 2 ** 31 
Example 1
Input
x = 9
y = 5
Output
2
Explanation
9 in binary is 1001 and 5 in binary is 0101, so indices 2 and 3 are different.
"""

class Solution:
    def solve(self, x, y):
        
        # x_bin = bin(x)[2:]
        # y_bin = bin(y)[2:]

        x_bin = '{:032b}'.format(x)
        y_bin = '{:032b}'.format(y)

        print(y_bin)
        count = 0
        for i in range(len(x_bin)):
            if x_bin[i] != y_bin[i]:
                count = count + 1
        
        return count
