# 941. Valid Mountain Array

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        
        size = len(A)
        # Check for edge cases
        if size < 3: return False
        
        up = []
        down = []
        decreasing = False
        
        for i in range(1, size):
            if A[i] > A[i-1] and not decreasing:
                up.append(A[i])
                
            elif A[i] == A[i-1]: return False
            else:
                decreasing = True
                down.append(A[i])
        
        # Check if both arrays are sorted. up in increasing order and down in decreasing order
        up_bool = all(up[i] < up[i+1] for i in range(len(up)-1)) and len(up) != 0
        down_bool = all(down[i] > down[i+1] for i in range(len(down) - 1)) and len(down) != 0
        
        return up_bool and down_bool
    
    
    # Note: An empty list is sorted. Look out for that
    
    
# LEETCODE SOLUTION
    
    
#     class Solution(object):
#     def validMountainArray(self, A):
#         N = len(A)
#         i = 0

#         # walk up
#         while i+1 < N and A[i] < A[i+1]:
#             i += 1

#         # peak can't be first or last
#         if i == 0 or i == N-1:
#             return False

#         # walk down
#         while i+1 < N and A[i] > A[i+1]:
#             i += 1

#         return i == N-1
