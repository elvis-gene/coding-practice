"""
Given a lowercase alphabet string s, return the index of the first recurring character in it. If there are no recurring characters, return -1.

Constraints

n ≤ 100,000 where n is the length of s
Example 1
Input
s = "abcda"
Output
4
Explanation
The a at index 4 is the first recurring character.

Example 2
Input
s = "abcde"
Output
-1
Explanation
No recurring characters in this string.

Example 3
Input
s = "aaaaa"
Output
1
Explanation
We want the first recurring character.
"""

class Solution:
    def solve(self, s):
        
        chars = []

        for i in range(len(s)):
            if s[i] in chars:
                return i
            else:
                chars.append(s[i])

        return -1
