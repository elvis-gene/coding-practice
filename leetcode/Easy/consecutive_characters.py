"""
1446. Consecutive Characters

Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

Return the power of the string.
 

Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.

Example 2:

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

Example 3:

Input: s = "triplepillooooow"
Output: 5

Example 4:

Input: s = "hooraaaaaaaaaaay"
Output: 11

Example 5:

Input: s = "tourist"

Output: 1
 
Constraints:

1 <= s.length <= 500
s contains only lowercase English letters.
"""
class Solution:
    def maxPower(self, s: str) -> int:
        
        # Algorithm:
        # Iterate through string keeping track of the current element being repeated
        # if next elements equals previous, increment count, get power
        # else, set count to 1 and curr_char to current character.
        # return power
        
        
        if len(s) == 1:
            return 1
        
        power = 0
        curr_char = s[0]    # l
        count = 1
        
        # Input: s = "leetcode"

        for i in range(1, len(s)):  # 6
            if s[i] == curr_char:   # d != o
                count += 1          # 1
            else:
                power = max(count, power)   # 2
                count = 1
                curr_char = s[i]    # o
        
        return max(power, count) # in case 'cc'
