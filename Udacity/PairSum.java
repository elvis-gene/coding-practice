/**
# Array Pair Sum

Given an integer array, output all pairs that sum up to a specific value k.
Consider the fact that the same number can add up to `k` with its duplicates in the array.

> For example the array is [1, 1, 2, 3, 4] and the desired sum is 4.
Should we output the pair (1, 3) twice or just once? Also do we output the reverse
of a pair, meaning both (3, 1) and (1, 3)? Let’s keep the output as short as possible
and print each pair only once. So, we will output only one copy of (1, 3).
Also note that we shouldn’t output (2, 2) because it’s not a pair of two distinct elements.

## Example
f(10, [3, 4, 5, 6, 7]) // [ [6, 4], [7, 3] ]
f(8, [3, 4, 5, 4, 4]) // [ [3, 5], [4, 4], [4, 4], [4, 4] ]
*/

import java.util.HashMap;
import java.util.Arrays;

class PairSum{

public static void function(int k, int [] array){
  HashMap <Integer, int[]> pairs = new HashMap<>();

  int counter = 1;
  StringBuilder strIdx = new StringBuilder();
  /** StringBuilder

  * To save index concatenations as strings. This will
  * help us not have index (1, 4) and (4, 1) in the
  * Hashmap.
  */

  for (int i = 0; i < array.length; i++) {
    for (int j = 0; j < array.length; j++) {

      if (!strIdx.toString().contains(String.valueOf(i+""+j)) &&
      !strIdx.toString().contains(String.valueOf(j+""+i))) {

        if (array[i] + array[j] == k && i != j) {
          pairs.put(counter, new int[]{array[i], array[j]});

          strIdx.append(i + "" +j);
          strIdx.append("-");
          counter++;
        }
      }
    }
  }

//This method is just to format the output.
StringBuilder outStr = new StringBuilder("[ ");
int hashCounter = 0;
  for(int key : pairs.keySet()){
    // System.out.prinln((Arrays.toString(pairs.get(key))));
    if (hashCounter < pairs.size() - 1) {
    outStr.append(Arrays.toString(pairs.get(key)));
    outStr.append(", ");
    hashCounter++;
      }
    else if (hashCounter == pairs.size() - 1){
      outStr.append(Arrays.toString(pairs.get(key)));
      outStr.append(" ]");
      hashCounter++;
     }
    }
    System.out.println(outStr.toString());
 }

public static void main(String [] args){
  int [] array = new int[]{3, 4, 5, 6, 7};
  function(10, array);
  }
}
