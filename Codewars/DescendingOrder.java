/*
    Your task is to make a function that can take any non-negative integer
    as a argument and return it with its digits in descending order.
    Essentially, rearrange the digits to create the highest possible number.

    Examples:
    Input: 21445 Output: 54421
    Input: 145263 Output: 654321
    Input: 123456789 Output: 987654321
 */

import java.util.Arrays;

public class DescendingOrder {
    public static int sortDesc(final int num) {
        //Your code
        String numStr = "" + num;
        int [] digits = new int[numStr.length()];
        StringBuilder finalNum = new StringBuilder();
        String aDigit;

            if (num > 0) {
                for (int i = 0; i < numStr.length(); i++) {
                    aDigit = "";
                    aDigit += numStr.charAt(i);
                    digits[i] = Integer.parseInt(aDigit);
                }

                Arrays.sort(digits);

                for (int i = digits.length - 1; i >= 0; i--) {
                    finalNum.append(digits[i]);
                }
            }else
                return 0;
        return Integer.parseInt(finalNum.toString());
    }

    public static void main(String [] args){
        System.out.println(sortDesc(145263));
    }
}

// Other solutions:

/*
import java.util.Comparator;
import java.util.stream.Collectors;

public class DescendingOrder {
    public static int sortDesc(final int num) {
        return Integer.parseInt(String.valueOf(num)
                                      .chars()
                                      .mapToObj(i -> String.valueOf(Character.getNumericValue(i)))
                                      .sorted(Comparator.reverseOrder())
                                      .collect(Collectors.joining()));
    }
}

import java.util.Arrays;
import java.util.Collections;

public class DescendingOrder {
    public static int sortDesc(final int num) {
        String[] array = String.valueOf(num).split("");
        Arrays.sort(array, Collections.reverseOrder());
        return Integer.valueOf(String.join("", array));
    }
}
 */