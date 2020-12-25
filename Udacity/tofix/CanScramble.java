/*
Write a function that returns true if one string can be formed out of another by
reordering ("scrambling") the characters.

For example:

```
can_scramble("abc", "cba") -> true
can_scramble("aab", "bba") -> false
```
*/

class CanScramble{
  public static boolean canScramble(String firstW, String secW){

    if (firstW.isEmpty() || secW.isEmpty() || firstW.length() != secW.length())
      return false;

    firstW = firstW.toLowerCase();
    secW = secW.toLowerCase();
    StringBuilder secWordStr = new StringBuilder(secW);
    int counter = 0; // If counter == firstW.length() then canSramble returns True

    for(int i = 0; i < firstW.length(); i++){
      // StringBuilder secWordStr = new StringBuilder(secW);

      for (int j = 0; j < secW.length(); j++) {
          if (String.valueOf(firstW.charAt(i)).equals(
            secWordStr.toString().charAt(j))) {

              counter++;
              secWordStr.delete(j, j+1); //This to avoid a BUG in the case where
                                        // we have repeated characters.
              break;
          }
      }
    }

    System.out.println(counter);

    boolean value = false;
    if (counter == firstW.length())
        value = true;

    return value;
  }

  public static void main(String [] args){
    System.out.println(canScramble("abc","cba"));
    System.out.println(canScramble("abb","bba"));
  }
}
