"""
You are given the logs for users' actions on LeetCode, and an integer k. The logs are represented by a 2D integer array logs where each logs[i] = [IDi, timei] indicates that 
the user with IDi performed an action at the minute timei.

Multiple users can perform actions simultaneously, and a single user can perform multiple actions in the same minute.

The user active minutes (UAM) for a given user is defined as the number of unique minutes in which the user performed an action on LeetCode. A minute can only be counted once, 
even if multiple actions occur during it.

You are to calculate a 1-indexed array answer of size k such that, for each j (1 <= j <= k), answer[j] is the number of users whose UAM equals j.

Return the array answer as described above.

 

Example 1:
Input: logs = [[0,5],[1,2],[0,2],[0,5],[1,3]], k = 5
Output: [0,2,0,0,0]
Explanation:
The user with ID=0 performed actions at minutes 5, 2, and 5 again. Hence, they have a UAM of 2 (minute 5 is only counted once).
The user with ID=1 performed actions at minutes 2 and 3. Hence, they have a UAM of 2.
Since both users have a UAM of 2, answer[2] is 2, and the remaining answer[j] values are 0.

Example 2:
Input: logs = [[1,1],[2,2],[2,3]], k = 4
Output: [1,1,0,0]
Explanation:
The user with ID=1 performed a single action at minute 1. Hence, they have a UAM of 1.
The user with ID=2 performed actions at minutes 2 and 3. Hence, they have a UAM of 2.
There is one user with a UAM of 1 and one with a UAM of 2.
Hence, answer[1] = 1, answer[2] = 1, and the remaining values are 0.
 

Constraints:

1 <= logs.length <= 104
0 <= IDi <= 109
1 <= timei <= 105
k is in the range [The maximum UAM for a user, 105].
"""

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        
        # Algorithm:
        # Get UAMs paired with their user IDs. Dictionary
        # create new list and populate it with values depending on the number of users with UAMs equal to the index starting at 1
        
        # Remove duplicated logs. See example 1
        logs_set = []
        for log in logs:
            if log not in logs_set:
                logs_set.append(log)
                
        # Get UAMs paired with their user IDs. format {ID, minute}        
        UAMs = {} 
        for log in logs_set:
            UAMs[log[0]] = UAMs.get(log[0], 0) + 1
        
        # Populate output array with zeros
        output = [0 for i in range(k)] 
        # Get UAMs/minutes from dictionary
        values = list(UAMs.values()) 
        
                
        # This for loop was used before I implemented the one below. This one cause a TLE
        # for i in range(1, k+1):
        #     output.append(values.count(i))
        
        for value in values:
            output[value-1] = output[value-1] + 1
        
        return output
