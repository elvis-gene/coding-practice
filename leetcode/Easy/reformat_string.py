"""
1417. Reformat The String

Given alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).

You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. 
That is, no two adjacent characters have the same type.

Return the reformatted string or return an empty string if it is impossible to reformat the string.

Example 1:
Input: s = "a0b1c2"
Output: "0a1b2c"
Explanation: No two adjacent characters have the same type in "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.
Example 2:

Input: s = "leetcode"
Output: ""
Explanation: "leetcode" has only characters so we cannot separate them by digits.

Example 3:
Input: s = "1229857369"
Output: ""
Explanation: "1229857369" has only digits so we cannot separate them by characters.

Example 4:
Input: s = "covid2019"
Output: "c2o0v1i9d"
Example 5:

Input: s = "ab123"
Output: "1a2b3"
 

Constraints:
1 <= s.length <= 500
s consists of only lowercase English letters and/or digits.
"""

class Solution:
    def reformat(self, s: str) -> str:
        
        # Algorithm:
        # check that the number of digits is either equal to the numbe of letters or one category's length is bigger.
        # than the other one by 1.
        # Then reformat by taking a character from each and forming a string.
        
        # Input: s = "a0b1c2"

        nums = [char for char in s if char.isnumeric()]         # [0, 1, 2]
        chars = [char for char in s if not char.isnumeric()]    # [a, b, c]
        
        # if not nums or not chars:
        #     return ''
        
        output = []
        
        if len(nums) - len(chars) in [-1, 0, 1]:
            
            if len(nums) > len(chars):
                output.append(nums[0])
                nums.pop(0)
                
                for num, char in zip(nums, chars):
                    output.append(char)
                    output.append(num)
            
            elif len(nums) < len(chars):
                output.append(chars[0])
                chars.pop(0)
                
                for num, char in zip(nums, chars):
                    output.append(num)
                    output.append(char)
            else:
                for num, char in zip(nums, chars):
                    output.append(num)
                    output.append(char)
        
        else:
            return ''

        return ''.join(output)
            

