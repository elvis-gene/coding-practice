"""
Given a string s and an integer k, return the number of k-length substrings that occur more than once in s.

Constraints

n ≤ 100,000 where n is the length of s.
k ≤ 10
Example 1
Input
s = "abcdabc"
k = 3
Output
1
Explanation
"abc" occurs twice in the string

Example 2
Input
s = "aaabbb"
k = 2
Output
2
Explanation
Both "aa" and "bb" occurs twice.
"""
class Solution:
    def solve(self, s, k):
        
        substrings_counts = {}

        for c in range(len(s)):
            substrings_counts[s[c:c+k]] = substrings_counts.get(s[c:c+k], 0) + 1
        
        count = 0
        for v in substrings_counts.values():
            if v > 1:
                count += 1
        
        return count

