# Number of Segments in a String

"""
Count the number of segments in a string, where a segment is defined
to be a contiguous sequence of non-space characters.
Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5
"""

class Solution:
    def countSegments(self, s: str) -> int:

        # Approach 1
        # return len(s.split())

        # Approach 2
        if len(s) == 0: return 0;
        if not s : return  0;  # For empty strings

        segments = s.split(" ")
        new_segments = [x for x in segments if str(x)]

        return len(new_segments)

        # To delete an element at a list index, use del [index]
