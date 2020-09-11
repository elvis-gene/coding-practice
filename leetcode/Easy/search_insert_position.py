""" 35. Search Insert Position

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # Algorithm: Compare target to each value of the list from left to right.
        # if it is inferior to the next value at the next index, it is at the right spoot.
        # if the superior to all the values in the list, it should be at len(nums)
        
        if target in nums:
            return nums.index(target)
        
        for i in nums:
            if target > i:
                continue
            else:
                return nums.index(i)
        
        return len(nums)
