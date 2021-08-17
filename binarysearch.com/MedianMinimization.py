"""

Given a list of integers nums, split it into two lists of equal size where the absolute difference between each list's median is as small as possible and return this difference.

Note: length of nums / 2 is guaranteed to be odd.

Constraints

n ≤ 100,000 where n is the length of nums
Example 1
Input
nums = [1, 9, 7, 4, 3, 6]
Output
2
Explanation
We can partition the list into [1, 4, 9] and [3, 6, 7]. Their medians are 4 and 6 and abs(4 - 6) = 2

"""

class Solution:
    def solve(self, nums):
        
        nums.sort()
        list_a = []
        list_b = []

        for i in range(len(nums)):
            if i % 2 == 0:
                list_a.append(nums[i]) 
            else:
                list_b.append(nums[i])

        median_a_index = len(list_a)//2
        median_b_index = len(list_b)//2

        return abs(list_a[median_a_index] - list_b[median_b_index])
