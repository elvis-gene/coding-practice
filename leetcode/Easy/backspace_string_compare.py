"""
844. Backspace String Compare

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
"""


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        # Algorithm:
        # using a stack/list, put each element into it unless it is #
        # if it is #, pop the element at the top of the stap which is the
        # the character just before the #
        
        
        def build_string(string: str):
            
            chars = []
            
            for c in string:
                if c == '#':
                    if chars: # check if list is not empty
                        chars.pop()
                else:
                    chars.append(c)
                
            return ''.join(chars)
        
        
        return build_string(S) == build_string(T)
            
