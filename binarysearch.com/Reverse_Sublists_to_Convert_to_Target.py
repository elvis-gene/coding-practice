"""
Reverse Sublists to Convert to Target

Given two lists of integers nums, and target, consider an operation where you take some sublist in nums and reverse it. Return whether it's possible to turn nums into target, given you can make any number of operations.

Constraints

0 ≤ n ≤ 100,000 where n is the length of nums
0 ≤ m ≤ 100,000 where m is the length of target
Example 1
Input
nums = [1, 2, 3, 8, 9]
target = [3, 2, 1, 9, 8]
Output
True
Explanation
We can reverse [1, 2, 3] and [8, 9]

Example 2
Input
nums = [10, 2, 3, 8, 9]
target = [3, 2, 1, 9, 8]
Output
False
"""

class Solution:
    def solve(self, nums):

        if len(nums) == 0:
            return False
        
        if nums[0] > nums[1]:
            return False

        # strictly = True
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return False
        
        return True
