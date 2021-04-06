"""
Palindromic Integer

Given a non-negative integer num, return whether it is a palindrome.

Bonus: Can you solve it without using strings?

Constraints

num < 2 ** 31

Example 1
Input
num = 121
Output
True

Example 2
Input
num = 20200202
Output
True

Example 3
Input
num = 43
Output
False
"""

class Solution:
    def solve(self, num):
        
        if num < 0:
            return False

        target = num
        pal = 0

        while num > 0:
            
            suf = num % 10 # 1
            pal = pal * 10 + suf 
            
            num = num//10

        return target == pal
