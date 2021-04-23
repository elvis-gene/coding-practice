"""
Longest Alliteration

Given a list of lowercase alphabet strings words, return the length of the longest contiguous sublist where all words share the same first letter.

Constraints:
0 ≤ n ≤ 100,000 where n is the length of words

Example 1:
Input:
words = ["she", "sells", "seashells", "he", "sells", "clams"]
Output:
3
Explanation:
["she", "sells", "seashells"] all share the first letter s.
"""

class Solution:
    def solve(self, words):
        
        if len(words) == 0:
            return 0

        # in case there's a minimum of a word in the list
        longest = 1
        counter = 1
        prev_prefix = words[0][0:1]

        for i in range(1, len(words)):
            if words[i].startswith(prev_prefix):
                counter = counter + 1
                longest = max(longest, counter)
            else:
                prev_prefix = words[i][0:1]
                counter = 1
        
        return longest
