class ArraySum {

  public static int sum(int [] array){

// Check if array is empty

    String str = array.toString();
    str = str.replaceAll("[\\[|]]", "");
    String [] arrayStr = str.split(",");
    int sum = 0;

    for(String num : arrayStr){
      // maybe check array has digits.
      sum += Integer.parseInt(num);
    }

    return sum;
  }

  public static void main(String [] args){
    // System.out.println(sum( new int[]{1,2,[3,4,[5]]}));
  }
}
