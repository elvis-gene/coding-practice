"""
Reverse Words

Given a string s of words delimited by spaces, reverse the order of words.

Constraints

n ≤ 100,000 where n is the length of s

Example 1
Input
sentence = "hello there my friend"
Output
"friend my there hello"
"""

class Solution:
    def solve(self, sentence):
        
        # Algorithm:
        # split string.
        # reverse list
        # join list

        words = sentence.split(' ')
        words = list(reversed(words))

        return ' '.join(words)
