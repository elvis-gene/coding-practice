"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
 
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:
0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # Algorithm:
        # Take the first word in the list
        # Initialise the current_prefix with the first letter of that word
        # Check that every other word starts with that letter
        # If they do, add letter to the prefix/result
        # concatenate the current_prefix with the next letter of that word 
        # then check if the rest of words also start with the current_prefix
        # and so on..
                
        if len(strs) == 0: return ''
        
        prefix = ''
        first_word = strs[0]   
        current_prefix = ''
        
        for l in first_word:   
            current_prefix += l 
            counter = 1
            
            for i in range(1, len(strs)):           
                if strs[i].startswith(current_prefix):  
                    counter += 1                    
                else:
                    return prefix
            
            if counter == len(strs):
                prefix += l
        
        return prefix
