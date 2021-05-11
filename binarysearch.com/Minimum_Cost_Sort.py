"""
Given a list of integers nums, return the minimum cost of sorting the list in ascending or descending order. The cost is defined as the sum of 
absolute differences between any element's old and new value.

Constraints

n ≤ 100,000 where n is the length of nums
Example 1
Input
nums = [1, 4, 3]
Output
2
Explanation
The cost to change the list to ascending order is 2:

Change 4 to 3 for a cost of 1
Change 3 to 4 for a cost of 1
Example 2
Input
nums = [7, 3, 5]
Output
4
Explanation
The cost to change the list to descending order is 4:

Change 3 to 5 for a cost of 2
Change 5 to 3 for a cost of 2
"""

class Solution:
    def solve(self, nums):
        
        sorted_nums_asc = sorted(nums)
        cost_asc = 0

        for i in range(len(nums)):
            cost_asc = cost_asc + abs(nums[i] - sorted_nums_asc[i])

        sorted_nums_desc = sorted(nums)
        sorted_nums_desc.sort(reverse=True)
        cost_desc = 0

        for i in range(len(nums)):
            cost_desc = cost_desc + abs(nums[i] - sorted_nums_desc[i])

        return min(cost_asc, cost_desc)

# Another solution
class Solution:
    def solve(self, nums):
        sorted_nums = sorted(nums)
        return min(
            sum(abs(b - a) for a, b in zip(nums, sorted_nums)),
            sum(abs(b - a) for a, b in zip(nums, reversed(sorted_nums))),
        )
