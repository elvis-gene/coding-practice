"""
Minimum String

You are given two strings s and t of equal length only consisting of lowercase letters. Assuming that you can first rearrange s into any order, return the minimum number of changes needed to turn s into t.

Constraints

0 ≤ n ≤ 100,000 where n is the length of s and t
Example 1
Input
s = "ehyoe"
t = "hello"
Output
2
Explanation
We can shuffle "ehyoe" to be "heyeo" and then turn "y" and the 2nd "e" into "l".
"""

class Solution:
    def solve(self, s, t):
     
        s_dict = {}
        t_dict = {}

        for x, y in zip(s, t):
            s_dict[x] = s_dict.get(x, 0) + 1
            t_dict[y] = t_dict.get(y, 0) + 1

        count = 0
        for key in t_dict.keys():
            if t_dict[key] > s_dict.get(key,0):
                count += t_dict[key] - s_dict.get(key,0)
        
        return count
       
