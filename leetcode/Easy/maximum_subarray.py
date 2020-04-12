"""
local_maximum at index i is the maximum of A[i]
and the sum of A[i] and local_maximum at index i-1.

for an array A
local_max[i] = max(A[i], A[i] + local_max[i - 1])
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = nums[0]
        maxs = list()
        maxs.append(maximum)

        for i in range(1, len(nums)):
            # maximum = max(maximum, 0) + nums[i]
            maximum = max(nums[i], nums[i] + maximum)
            maxs.append(maximum)

        return max(maxs)


# Alternative solution without using a list
def largest_continous(l):
    """
    Runtime: O(n)
    """
    max_sum = 0
    start = 0
    end = 1
    while (end <= len(l)):
        if l[start] + l[start+1] > 0:
            curr_sum = sum(l[start:end])
            max_sum = max(curr_sum, max_sum)
            end += 1
        else:
            # Start new sequence
            start = end + 1
            end = start + 1
    return max_sum

print largest_continous([5,-2,6,-3,12,24,-1,1,3])
