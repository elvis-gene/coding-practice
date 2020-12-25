class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        # Algorithm:
        # Remove the number of coins that has to be used
        # for each row from n until its either zero or negative.
        
        if not n: return 0
        
        i = 1
        complete_stairs = 0
        
        while (n > 0):
            n -= i
            
            if n >= 0:
                complete_stairs += 1

            i += 1
            
                
        return complete_stairs
            
