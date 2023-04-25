import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scan = new Scanner(System.in);
        String A = scan.next();
        int count = 0;
        for (int i = 0; i < (int) A.length()/2; i++) {
          if (A.charAt(i) == A.charAt(A.length() - i - 1)) {
            count++;
          }
        }
        
        if (count == (int) A.length()/2) {
          System.out.print("Yes");
        } else {
          System.out.print("No");
        }
        scan.close(); // Close Scanner object
    }
}
