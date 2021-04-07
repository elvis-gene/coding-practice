"""
Find Local Peaks

You are given a list of integers nums. Return the index of every peak in the list, sorted in ascending order. An index i is called a peak if

nums[i] > nums[i + 1] if i = 0
nums[i] > nums[i - 1] if i = n - 1
nums[i - 1] < nums[i] > nums[i + 1] otherwise
However, a list of length 1 is not considered a peak.

Constraints

0 ≤ n ≤ 100,000 where n is the length of nums

Example 1
Input
nums = [1, 2, 3, 2, 4]
Output
[2, 4]
Explanation
The values at index 2 and 4 are considered peaks since they are larger than their neighbors.

Example 2
Input
nums = [1, 1, 1, 1]
Output
[]

Example 3
Input
nums = [5]
Output
[]

Example 4
Input
nums = [3, 4]
Output
[1]
"""

class Solution:
    def solve(self, nums):

        if len(nums) == 1:
            return []
        
        peaks = []
        n = len(nums)

        for i in range(n):  

            if i == 0:
                if nums[i] > nums[i + 1]:
                    peaks.append(i)
            elif i == n - 1:
                if nums[i] > nums[i - 1]:
                    peaks.append(i)
            elif nums[i - 1] < nums[i] > nums[i + 1]:
                peaks.append(i)
        
        return peaks
