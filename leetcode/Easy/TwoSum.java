class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        int [] indices = new int[2];
        boolean found = false;
        
        for (int i = 0; i < nums.length; i++){
            for (int j = 0; j < nums.length; j++){
                
                if(i != j) // To not include unnecessary comparsons. And You may not use the same element twice
                if (nums[i] + nums[j] == target){
                    found = true;
                    indices[0] = i;
                    indices[1] = j;
                    
                    // System.out.println(i + ", " + j);
                    break;
                }
            }
            if(found)
            break;
        }
         return indices;
    }
    
    public static void main(String [] args){
        Solution sol = new Solution();
        
        int [] nums = {11, 2, 7, 15};
        sol.twoSum(nums, 9);
    }
}

/**
Top Submission using less time - 0ms

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int Volume = 2048;      //100000000000
        int bitMode = Volume-1; //011111111111
        int[] t = new int[Volume]; //store index+1, in order to skip default 0
        int i = 0, c = 0;
        for (i = 0; i < nums.length; i++)
        {
            c = (target - nums[i]) & bitMode; 
            if (t[c] != 0)  
                break;
            t[nums[i] & bitMode] = i + 1;
        }
        return new int[] { t[c] - 1, i };
    }
}
*/