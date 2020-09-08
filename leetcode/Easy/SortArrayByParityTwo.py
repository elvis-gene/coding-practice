"""
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.
Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.
You may return any answer array that satisfies this condition.

Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
 

Note:

2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000
"""

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        
        # Algorithm: Seperate the input array in two different arrays, one of odd and the other
        # of even numbers. Then Take an element from left and another from the right of the array while merging the final list
        
        odd_nums = [num for num in A if num % 2 != 0]
        even_nums = [num for num in A if num %2 == 0]
        merged_nums = list()
        merged_nums.extend(even_nums)
        merged_nums.extend(odd_nums)
        
        h_size = int(len(A)/2)
        size = len(A) - 1 # To access the list from the back
        target = list()
        
        for i in range(h_size):
            target.append(merged_nums[i])
            target.append(merged_nums[size])
            size -= 1
        
        return target
            
            
        # Time complexity: O(N) + O(N) + O(N/2) => O(N)
        
            
        
        
