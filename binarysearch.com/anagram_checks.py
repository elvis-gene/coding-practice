"""
Anagram Checks

Given two strings s0 and s1, return whether they are anagrams of each other.

Constraints

n ≤ 100,000 where n is the length of s0
m ≤ 100,000 where m is the length of s1

Example 1
Input
s0 = "listen"
s1 = "silent"
Output
True

Example 2
Input
s0 = "bedroom"
s1 = "bathroom"
Output
False
"""

class Solution:
    def solve(self, s0, s1):
        
        s0_list = [c for c in s0]
        s1_list = [c for c in s1]

        s0_list.sort()
        s1_list.sort()

        return s0_list == s1_list
