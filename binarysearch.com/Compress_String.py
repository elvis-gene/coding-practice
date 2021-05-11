"""
Given a string lowercase alphabet s, eliminate consecutive duplicate characters from the string and return it.

That is, if a list contains repeated characters, they should be replaced with a single copy of the character. The order of the elements should not be changed.

Constraints

0 ≤ n ≤ 100,000 where n is the length of s
Example 1
Input
s = "aaaaaabbbccccaaaaddf"
Output
"abcadf"
Example 2
Input
s = "a"
Output
"a"
"""

class Solution:
    def solve(self, s):
        
        # When the string is empty or has one character, return as is
        if len(s) < 2:
            return s

        chars = [c for c in s]
        left, right = 0, 1

        while right <= len(chars) -1:
            if chars[left] == chars[right]:
                chars.pop(right)
            else:
                left = left + 1
                right = right + 1

        return ''.join(chars)
