"""
67. Add Binary

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Approach 1: Runtime: 52 ms, faster than 6% of Python submissions
        # Converting both strings to decimal first,
        # add both numbers then convert the answer to binary

        a_len = len(a)
        b_len = len(b)
        num_a = 0
        num_b = 0
        exp_a = 0
        exp_b = 0

        for i in reversed(range(a_len)):
            num_a += int(a[i]) * 2 ** exp_a  # ** = pow, ^ = exponent
            exp_a += 1


        for i in reversed(range(b_len)):
            num_b += int(b[i]) * 2 ** exp_b
            exp_b += 1

        print ('{}, {}'.format(num_a, num_b))
        return bin(num_a + num_b)[2:]


        # Approach 2: Runtime: 28 ms, faster than 84.10% of Python submissions
        # Adding both binary numbers straight away

    def addBinary(self, a: str, b: str) -> str:
        a = int(a, base=2)
        b = int(b, base=2)
        # return format(a+b, 'b')
        return bin(a+b)[2:]
