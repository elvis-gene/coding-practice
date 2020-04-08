public class ReverseString {
    public static void main(String[] args) {
        System.out.println(revString("Presley"));

        System.out.println(revStringWithSBuilder("Gene"));
    }

    public static String revString(String str){
        String revStr = "";

        for (int i = str.length() - 1; i >= 0; i--){ //TODO: Why is it --i in the solution?
            revStr += str.charAt(i);
        }
        return revStr;
    }

    public static String revStringWithSBuilder(String str){
        int len = str.length();
        StringBuilder revStr = new StringBuilder(len);

        for (int i = len - 1; i >= 0; i--)
            revStr.append(str.charAt(i));

        return revStr.toString(); //TODO: What is the advantage of using 'StringBuilder' over 'new String'
    }
}


