/*
Calculate the number of "loops" in a number.
A number has a loop when it has a closed circle when you draw it, so
6 has one loop, 1 has no loop and 8 has two loops.
So 2876 has three loops

*/

import java.util.HashMap;

class NumLoopCounter{
public static int loopCounter(int num){
    HashMap<Integer, Integer> numAndValue =
    new HashMap<>();

    numAndValue.put(0,0);
    numAndValue.put(1,0);
    numAndValue.put(2,0);
    numAndValue.put(3,0);
    numAndValue.put(4,0);
    numAndValue.put(5,0);
    numAndValue.put(6,1);
    numAndValue.put(7,0);
    numAndValue.put(8,2);
    numAndValue.put(9,1);

    String numsString = num + "";
    int counter = 0;
    for (int i = 0; i < numsString.length(); i++) {
        counter += numAndValue.get(Integer.parseInt(String.valueOf(numsString.charAt(i))));
    }

    return counter;
  }

  public static void main(String [] args){
    System.out.print(loopCounter(2876));
  }
}
