"""
Given a string s consisting only of "1"s and "0"s, you can delete any two adjacent letters if they are different.

Return the length of the smallest string that you can make if you're able to perform this operation as many times as you want.

Constraints

0 ≤ n ≤ 100,000 where n is the length of s
Example 1
Input
s = "11000"
Output
1
Explanation
After deleting "10" we get "100" and we can delete another "10" to get "0" which has a length of 1.
"""

class Solution:
    def solve(self, s):
        
        # Using a stack
        liste = []

        for c in s:
            if not liste or liste[-1] == c:
                liste.append(c)
            elif liste[-1] != c:
                liste.pop()

        return len(liste)

