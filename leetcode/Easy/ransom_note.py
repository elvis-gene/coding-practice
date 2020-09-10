class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        """
        Given an arbitrary ransom note string and another string containing letters from all the magazines, 
        write a function that will return true if the ransom note can be constructed from the magazines; 
        otherwise, it will return false.

        Each letter in the magazine string can only be used once in your ransom note.

        Example 1:

        Input: ransomNote = "a", magazine = "b"
        Output: false
        Example 2:

        Input: ransomNote = "aa", magazine = "ab"
        Output: false
        Example 3:

        Input: ransomNote = "aa", magazine = "aab"
        Output: true


        Constraints:

        You may assume that both strings contain only lowercase letters.
        """
        
    
#         Algorithm:
#                 Check wether each value of ransomNote is in
#                 magazine. When a value is in magazine, remove
#                 it from magazine and keep iterating.
                
        
        
        output = True
        mag_list = list()
        mag_list[:0] = magazine
        
        for l in ransomNote:
            if l in mag_list:
                mag_list.remove(l)
            else:
                output = False
        
        return output
    

        # Time complexity: O(n x m), n being the number 
        # of elements in ransomNote and m in magazine
