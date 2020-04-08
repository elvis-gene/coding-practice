"""
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in
the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Approach:
        # Try to save all the List elements into a Set.
        # At the end of it, if both the Set & List have different lenghts,
        # return False otherwise True.

        list_size = len(nums)
        # set_nums = {num for num in nums}
        set_nums = set(nums)
        set_size = len(set_nums)

        if list_size == set_size: return False
        else: return True
