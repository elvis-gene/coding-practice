"""
Given a list of integers nums, sort the array such that:

All even numbers are sorted in increasing order
All odd numbers are sorted in decreasing order
The relative positions of the even and odd numbers remain the same
Constraints

n ≤ 100,000 where n is the length of nums
Example 1
Input
nums = [8, 13, 11, 90, -5, 4]
Output
[4, 13, 11, 8, -5, 90]
Explanation
The even numbers are sorted in increasing order, the odd numbers are sorted in decreasing number, and the relative positions 
were [even, odd, odd, even, odd, even] and remain the same after sorting.
"""

class Solution:
    def solve(self, nums):
        
        odds = [num for num in nums if num%2 != 0]
        # Sort odds in descending order
        odds.sort(reverse=True)

        evens = [num for num in nums if num%2 == 0]
        # Sort evens in ascending order
        evens.sort()

        output = []

        for num in nums:
            if num%2 == 0:
                output.append(evens[0])
                evens.pop(0)
            else:
                output.append(odds[0])
                odds.pop(0)

        return output
        
