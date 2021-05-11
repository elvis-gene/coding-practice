"""
Given a list of integers nums, return whether all numbers appear an even number of times.

This should be done in \mathcal{O}(1)O(1) space.

Constraints

n ≤ 100,000 where n is the length of nums
Example 1
Input
nums = [2, 4, 4, 2, 3, 3]
Output
True
Explanation
Every number occurs twice.

Example 2
Input
nums = [1]
Output
False
Explanation
1 occurs an odd number of times.
"""

class Solution:
    def solve(self, nums):
        
        if len(nums) < 2:
            return False

        nums.sort()
        count = 1
        prev = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] == prev:
                count = count + 1
                prev = nums[i]
            else:
                if count%2 != 0:
                    return False
                prev = nums[i]
                count = 1
        
        return count % 2 == 0
        
