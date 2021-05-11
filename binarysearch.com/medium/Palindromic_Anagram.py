"""
Given a string s, determine whether any anagram of s is a palindrome.

Constraints

n ≤ 100,000 where n is the length of s
Example 1
Input
s = "carrace"
Output
True
Explanation
"carrace" should return true, since it can be rearranged to form "racecar", which is a palindrome.
"""

class Solution:
    def solve(self, s):
        """
        Note: 
        A property of a palindrome is that it can have at most one unique 
        character that occurs odd number of times.
        """

        pairs = {}
        for c in s:
            pairs[c] = pairs.get(c, 0) + 1

        occurs = pairs.values()
        odds_count = 0
        for num in occurs:
            if num % 2 != 0:
                odds_count += 1

                if odds_count > 1:
                    return False
        return True
