/*
345. Reverse Vowels of a String

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Input: "hello"
Output: "holle"

Example 2:
Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".

*/

class Solution {
    public String reverseVowels(String s) {
        
        if (s.isEmpty())
        return s;
        
          int left = 0;				      
          int right = s.length() - 1;		

          String vowels = "aoiueAOIUE";
          char [] s_chars = s.toCharArray();

          while(left < right){				    
            if (vowels.indexOf(s_chars[left]) >= 0 && vowels.indexOf(s_chars[right]) >= 0){
                char temp = s_chars[left];		
                s_chars[left] = s_chars[right];	
                s_chars[right] = temp;			
                right--;
                left++;
            }
            else if(vowels.indexOf(s_chars[left]) >= 0){
              right--;
            }
            else if(vowels.indexOf(s_chars[right]) >= 0){
              left++;
            }
            else{
              left++;
              right--;
            }
          }

          return String.valueOf(s_chars);
        }
}

