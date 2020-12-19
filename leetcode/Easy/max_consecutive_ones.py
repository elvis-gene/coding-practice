"""
485. Max Consecutive Ones

Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
The maximum number of consecutive 1s is 3.


Note:
The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        # Algorithm:
        # Have a variable called count
        # By iterating through the list, increment count whenever there is a 1
        # otherwise add count to a list count to zero and set it to zero.
        # return the highest number of the list.
        
        # if not nums: 
        #     return 0
        
        # [1,1,0,1,1,1]     Test
        
        count = 0
        consecutives = []
        for num in nums:    # [1, 1, 0]
            if num == 1:
                count += 1  # count = 2
            else:
                consecutives.append(count)  # [2, ]
                count = 0
        
        consecutives.append(count)  # Very important part to think about.
        
        return max(consecutives)
