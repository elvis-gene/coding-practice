"""
41. First Missing Positive

Given an unsorted integer array nums, find the smallest missing positive integer.
Follow up: Could you implement an algorithm that runs in O(n) time and uses constant extra space.?

Example 1:
Input: nums = [1,2,0]
Output: 3

Example 2:
Input: nums = [3,4,-1,1]
Output: 2

Example 3:
Input: nums = [7,8,9,11,12]
Output: 1

Constraints:
0 <= nums.length <= 300
-231 <= nums[i] <= 231 - 1
"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        if len(nums) == 0: 
            return 1
        if len(nums) == 1 and nums[0] < 1:
            return 1

        nums.sort()
        positive_nums = [num for num in nums if num > 0] # Get rid of all the negative numbers.
        
        numbers = set()
        if len(positive_nums) > 0:
            if positive_nums[0] != 1:
                return 1
            else:
                numbers.add(positive_nums[0])
        
        
        for i in range(1, len(positive_nums)):
            if positive_nums[i] > positive_nums[i-1] + 1:
                return positive_nums[i-1] + 1
            else:
                numbers.add(positive_nums[i])
        
        
        if len(numbers) == 0: return 1  # In case all the numbers are negative
        else: return max(numbers) + 1   # In the case of ordered positive numbers with no number missing in between them
                    
