/*
    An isogram is a word that has no repeating letters, consecutive or non-consecutive.
    Implement a function that determines whether a string that contains only letters is an isogram.
    Assume the empty string is an isogram. Ignore letter case.

    isIsogram "Dermatoglyphics" == true
    isIsogram "aba" == false
    isIsogram "moOse" == false -- ignore letter case
 */

public class Isograms {
    public static boolean  isIsogram(String str) {

        if (str.isEmpty())
            return true;

        int count = 0;

        for (int i = 0; i < str.length(); i++){
            for (int j = 0; j < str.length(); j++){
                if (i != j)
                if (String.valueOf(str.charAt(i))
                        .equalsIgnoreCase(String.valueOf(str.charAt(j)))) {
                    count++;
                    break;
                }
            }
            if (count != 0)
                break;
        }

        return count == 0;
    }

    public static void main(String[] args) {

        System.out.println(isIsogram("Dermatoglyphics"));
        System.out.println(isIsogram("isogram"));
        System.out.println(isIsogram("moose"));
        System.out.println(isIsogram("isIsogram"));
        System.out.println(isIsogram("aba"));
        System.out.println(isIsogram("moOse"));
        System.out.println(isIsogram("thumbscrewjapingly"));
        System.out.println(isIsogram(""));
    }
}

/*
    OTHER SOLUTIONS:
    #1 : The number of characters in the string must be equal to the number of
            distinctive characters.

    public class isogram {
    public static boolean  isIsogram(String str) {
    return str.length() == str.toLowerCase().chars().distinct().count();



    #2 : USING AN HASHSET

    import java.util.HashSet;
import java.util.Set;

public class isogram {
  public static boolean isIsogram(String str) {
    Set<Character> letters = new HashSet<Character>();

    for (int i = 0; i < str.length(); ++i) {
      if (letters.contains(str.toLowerCase().charAt(i))) {
        return false;
      }

      letters.add(str.charAt(i));
    }

    return true;
  }
}

  }
}
 */
