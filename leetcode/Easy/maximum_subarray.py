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
