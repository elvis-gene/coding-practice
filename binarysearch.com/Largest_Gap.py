"""
Largest Gap

Given a list of integers nums, return the largest difference of two consecutive integers in the sorted version of nums.

Constraints

n ≤ 100,000 where n is the length of nums

Example 1
Input
nums = [4, 1, 2, 8, 9, 10]
Output
4

Explanation
The largest gap is between 4 and 8.
"""

class Solution:
    def solve(self, nums):
        
        nums.sort()
        max_gap = 0

        for i in range(len(nums)-1):

            gap = nums[i+1] - nums[i]
            max_gap = max(max_gap, gap)
        
        return max_gap
