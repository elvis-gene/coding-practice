"""
Detect the Only Duplicate in a List

You are given a list nums of length n + 1 picked from the range 1, 2, ..., n. By the pigeonhole principle, there must be a duplicate. Find and return it. 
There is guaranteed to be exactly one duplicate.

Bonus: Can you do this in \mathcal{O}(n)O(n) time and \mathcal{O}(1)O(1) space?

Constraints

n ≤ 10,000
Example 1
Input
nums = [1, 2, 3, 1]
Output
1
Example 2
Input
nums = [4, 2, 1, 3, 2]
Output
2

"""


class Solution:
    def solve(self, nums):
        
        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return nums[i]
        
