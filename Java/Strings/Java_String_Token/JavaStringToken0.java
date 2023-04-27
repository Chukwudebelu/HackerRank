import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine().trim();
        scan.close(); // close Scanner Object
        
        if (s.equals("")) { // if s is an empty String ""
          System.out.print(s.length()); // 0
        } else {
          // Split string using the non-alphanumeric characters as delimiters
          String[] tokens = s.split("[ !,?._'@]+");
          System.out.println(tokens.length);
          // for-each loop print each token
          for (String token: tokens) {
            System.out.println(token);
          }
        }
    }
}

