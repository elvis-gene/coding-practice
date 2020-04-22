# 557. Reverse Words in a String III
"""
Given a string, you need to reverse the order of characters in each word
within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Note: In the string, each word is separated by single space
 and there will not be any extra space in the string.
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        # Approach 1:
        # Put every word in a list then reverse each of them seperately
        if not s: return ''

        words_list = s.split(' ')
        reversed_words_list = [x[::-1] for x in words_list]

        return ' '.join(reversed_words_list)

# shorter:  return " ".join([i[::-1] for i in s.split()])


# Java solution

# public class Solution {
#     public String reverseWords(String s) {
#         String words[] = s.split(" ");
#         StringBuilder res=new StringBuilder();
#         for (String word: words)
#             res.append(new StringBuffer(word).reverse().toString() + " ");
#         return res.toString().trim();
#     }
# }
