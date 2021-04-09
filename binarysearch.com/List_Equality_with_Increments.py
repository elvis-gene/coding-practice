"""
List Equality with Increments

You are given a list of integers nums, and want to make the values equal. Consider an operation where you pick an integer in the list and increment every other value .

Return the minimum number of operations required to make integer values equal.

Constraints
n ≤ 100,000 where n is the length of nums

Example 1
Input
nums = [1, 3, 4]
Output
5

Explanation
Here are the operations we can use:

[2, 4, 4]
[3, 5, 4]
[4, 5, 5]
[5, 6, 5]
[6, 6, 6]
"""

class Solution:
    def solve(self, nums):
        
        # Algorithm:
        # The difference between each value in list to the minimum is the number
        # of decrements by 1 it will take that number to reach that minimum.
        # if you add all the differences, you will find the answer of the problem

        min_v = min(nums)
        count = 0

        for num in nums:
            count = count + num - min_v

        return count
