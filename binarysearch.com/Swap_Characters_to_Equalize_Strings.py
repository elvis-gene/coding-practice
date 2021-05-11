"""
You are given two lowercase alphabet strings s and t, both of them the same length. You can pick one character in s and another in t and swap them. 
Given you can make unlimited number of swaps, return whether it's possible to make the two strings equal.

Constraints

n ≤ 100,000 where n is the length of s and t
Example 1
Input
s = "ab"
t = "ba"
Output
True
Example 2
Input
s = "aa"
t = "aa"
Output
True

"""

class Solution:
    def solve(self, s, t):
        
        # The two strings can be equal after swaps if
        # all characters have an even count

        merge = s+t
        pairs = {}

        for c in merge:
            pairs[c] = pairs.get(c,0) + 1
        
        counts = pairs.values()
        
        for num in counts:
            if num % 2 != 0:
                return False
        
        return True

        

