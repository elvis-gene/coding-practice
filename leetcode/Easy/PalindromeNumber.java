/*
Determine whether an integer is a palindrome.
An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left,
it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
*/

class palindromeNumber {
    public boolean isPalindrome(int x) {
        int input = x;

        if(x == 0)
            return true;

        if(x < 0)
            return false;

        int revNum = 0;
        while(x != 0){
            int popped = x % 10;
            x /= 10;

            // Avoiding integer overflow
            if(revNum > Integer.MAX_VALUE/ 10 || (revNum == Integer.MAX_VALUE/10 && popped > 7))
                return false;
            if(revNum < Integer.MIN_VALUE / 10 || (revNum == Integer.MIN_VALUE /10 && popped < -8))
                return false;

            revNum = revNum * 10 + popped;
        }

        return revNum == input;
    }
}
