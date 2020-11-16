"""
125. Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: "race a car"
Output: false
 

Constraints:
s consists only of printable ASCII characters.
"""


import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # Remove characters and spaces and convert input string to lower case
        s = re.sub('[^0-9a-zA-Z]+', '', s)
        s = re.sub(' ', '', s)
        s = s.lower()

        # Approach 1: using two pointers
        # Compare the first element of the string with the last one and so on
        
        start = 0
        end = len(s) - 1
        s_size = len(s)
        
        for i in range(int(s_size/2)):
            if s[start] != s[end]:
                return False
            else:
                start += 1
                end -= 1
        
        return True
    
        # O(n/2) ─> O(n)
 
# Approach 2: Reversing the string
import re

class Solution(object):
    def isPalindrome(self, s):
        
        s = re.sub('[^0-9a-zA-Z]+', '', s)
        s = re.sub(' ', '', s)
        s = s.lower()
        
        return s == s[::-1]
        
