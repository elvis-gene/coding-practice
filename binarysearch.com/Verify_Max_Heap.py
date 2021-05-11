"""
Given a list of integers nums, return whether it represents a max heap. That is, for every i we have that:

nums[i] ≥ nums[2*i + 1] if 2*i + 1 is within bounds
nums[i] ≥ nums[2*i + 2] if 2*i + 2 is within bounds
Constraints

0 ≤ n ≤ 100,000 where n is the length of nums
Example 1
Input
nums = [4, 2, 3, 0, 1]
Output
True
"""

class Solution:
    def solve(self, nums):

        size = len(nums)

        for i in range(size):
            
            if 2*i+1 < size:
                if not nums[i] >= nums[2*i + 1]:
                    return False
            
            if 2*i+2 < size:
                if not nums[i] >= nums[2*i + 2]:
                    return False
            
        return True
