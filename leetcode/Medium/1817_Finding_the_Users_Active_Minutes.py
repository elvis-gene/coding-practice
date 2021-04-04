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
