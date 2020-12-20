"""
1544. Make The String Great

Given a string s of lower and upper case English letters.
A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.

 

Example 1:
Input: s = "leEeetcode"
Output: "leetcode"
Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".

Example 2:
Input: s = "abBAcC"
Output: ""
Explanation: We have many possible scenarios, and all lead to the same answer. For example:
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""

Example 3:
Input: s = "s"
Output: "s"
 

Constraints:

1 <= s.length <= 100
s contains only lower and upper case English letters.
"""

class Solution:
    def makeGood(self, s: str) -> str:
        
        # Algorithm:
        # To check that 2 characters are the same but have different cases,
        # check that the numerical values are different but when converted to 
        # lower case for instance, they are equal. 
        # Then remove those letters.
        
        if not s:
            return s
        
        output = []
        
        for i in range(len(s)): # l
            
            if output:
                if s[i].lower() == output[-1].lower() and ord(s[i]) != ord(output[-1]):
                    output.pop();
                else:
                    output.append(s[i]) 
            else:
                output.append(s[i])    
        
        return ''.join(output)
