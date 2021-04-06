"""
Consecutive Ones

You are given a list of integers nums which contains at least one 1. Return whether all the 1s appear consecutively.

Constraints

1 ≤ n ≤ 100,000 where n is the length of nums

Example 1
Input
nums = [0, 1, 1, 1, 2, 3]
Output
True
Explanation
All the 1s appear consecutively here in the middle.

Example 2
Input
nums = [1, 1, 0, 1, 1]
Output
False
Explanation
There's two groups of consecutive 1s.
"""

class Solution:
    def solve(self, nums):
        
        num_ones = nums.count(1)
        
        # [1, 1, 0, 1, 1]
        
        count = 0

        for num in nums:
            if num == 1:
                count = count + 1

                if count == num_ones:
                    return True

            elif num != 1 and count > 0:
                count = count - 1
        
        return False
