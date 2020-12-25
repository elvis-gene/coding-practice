"""
414. Third Maximum Number

Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.

Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
"""

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        # Algorithm:
        # Remove duplicates
        # If the remaining list has less than 3 characters, return max
        # Find and remove largest number
        # Find and remove the second largest number
        # Return max, which is the third largest number
        
        l = set(nums)
        
        if len(l) < 3: 
            return max(l)
        
        l.remove(max(l))
        l.remove(max(l))

        return max(l)
