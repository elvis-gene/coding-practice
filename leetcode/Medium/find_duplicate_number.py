"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one duplicate number in nums, return this duplicate number.

Follow-ups:

How can we prove that at least one duplicate number must exist in nums? 
Can you solve the problem without modifying the array nums?
Can you solve the problem using only constant, O(1) extra space?
Can you solve the problem with runtime complexity less than O(n2)?

Constraints:

2 <= n <= 3 * 104
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # How can we prove that at least one duplicate number must exist in nums? 
        # Comparing max(nums) and len(nums). If len(nums) if bigger than max(nums) by 1 then there must be a duplicate since [1, n]


        # Algorithm:
        # Sort list then compare each element next to another
    
        nums.sort()
        size = len(nums) # Rather put in in loop?
        
        for i in range(0, size - 1):
            if nums[i] == nums[i+1]:
                return nums[i]
        
        @ O(nlgn)

# Another solution using a set
class Solution:
    def findDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
     # O(n)
