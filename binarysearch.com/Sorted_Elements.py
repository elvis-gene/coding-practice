"""
Sorted Elements

Give a list of numbers nums, return the number of elements that are in the correct indices, if the list were to be sorted.

Constraints

n ≤ 100,000 where n is the length of nums
Example 1
Input
nums = [1, 7, 3, 4, 10]
Output
2

Explanation
Comparing nums and its sorted version we find that elements 1 and 10 are in their correct positions.

[1, 7, 3, 4, 10]
[1, 3, 4, 7, 10]
"""

class Solution:
    def solve(self, nums):
        
        nums_sorted = sorted(nums)
        count = 0

        for i in range(len(nums)):
            if nums_sorted[i] == nums[i]:
                count = count + 1
            
        return count
