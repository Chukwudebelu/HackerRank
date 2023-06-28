//!/bin/java
import java.util.*;

public class Solution {
    public static void main(String[] args) {
        /*E nter your code here. Read input from STDIN. Print output to STDOUT. Your class should benamed Solution. */ 
        Scanner scan = new Scanner(System.in);
        String A = scan.next();
        String B = scan.next();
      
        // Sum lengths of A & B
        int n = A.length() + B.length();
        System.out.println(n);
        
        // Lexicographical/Alphabetical order
        int order = A.compareTo(B);
        
        if (order > 0)
          System.out.println("Yes");
        else
          System.out.println("No");
        
        // Capitalize the 1st letter
        System.out.println(A.substring(0,1).toUpperCase() + A.substring(1) + " " + B.substring(0,1).toUpperCase() + B.substring(1));
    }
}
