class DuplicateZeros {
/*        public void duplicateZeros(int[] arr) {
        int arrLength = arr.length;

        for (int i = 0; i < arrLength; i++){
            if (arr[i] == 0){
                for (int j = arrLength - 1; j >= i+1; j--){
                    arr[j] = arr[j-1];
                }

                if (i<arrLength-1)  // If there is already a zero at the end, leave it as is
                arr[i+1] = 0;
                i++; // Ignore the duplicated zero
            }
        }
    }
*/

    // With a different style of looping. Might be easier to  understand
    public void duplicateZeros(int[] arr) {
        int arrLength = arr.length;

        for (int i = 0; i < arrLength; i++){
            if (arr[i] == 0){
                for (int j = arrLength - 2; j >= i; j--){
                    arr[j+1] = arr[j];
                }

                if (i<arrLength-1)  // If there is already a zero at the end, leave it as is
                    arr[i+1] = 0;
                i++; // Ignore the duplicated zero
            }
        }
    }

    // Top solution on LeetCode

/*    class Solution {
    public void duplicateZeros(int[] arr) {
        int[] temp = Arrays.copyOf(arr, arr.length);

        for(int i = 0, j = 0; i < arr.length; i++, j++) {
            if(temp[j] == 0) {
                arr[i] = 0;
                i++;
                if(i < arr.length) {
                    arr[i] = 0;
                }
            } else {
                arr[i] = temp[j];
            }
        }
    }
} */
}
