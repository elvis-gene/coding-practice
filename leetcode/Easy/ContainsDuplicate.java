/*
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice
in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
*/


import java.util.Arrays;

class containsDuplicate {
    public boolean containsDuplicate(int[] nums) {

        if(nums.length == 0)
            return false;

        Arrays.sort(nums);
        boolean containsDup = false;

        //Only one pass will be necessary
        for (int i = 0; i < nums.length; i++){
            if(i < nums.length - 1)
            if(nums[i] == nums[i + 1])
                containsDup = true;
        }

        return containsDup;
    }
}
