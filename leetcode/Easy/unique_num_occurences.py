"""
Given an array of integers arr, write a function that returns true if and only
if the number of occurrences of each value in the array is unique.


Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
 

Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
"""

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        """
        Algorithm:
                Get the count (number of occurences) of each element in the list 
                and add it to a set. If the set has a different 
                size compared to the number of unique elements in the list, return False
        """
        if len(arr) == 1:
            return True
        
        occurences = set()
        for num in arr:
            occurences.add(arr.count(num))
        
        return len(occurences) == len(set(arr))
    
        
        # Algorithm 2: using hashmap
        # save each count with its number
        # before saving check if that count (existing count + 1) exists
        # if it does return False.
        
        # Input: arr = [1,2,2,1,1,3]
            
        occur_map = dict()
        occurences = []
        
        for num in arr: # 3
            occur_map[num] = occur_map.get(num, 0) + 1 # {1 : 3, 2 : 2, 3 : 1}
        
        for value in occur_map.values():
            if value in occurences:
                return False
            else:
                occurences.append(value)
        
        return True
