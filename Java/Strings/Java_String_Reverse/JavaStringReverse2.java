import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        String A = sc.next();
        String A_reverse = "";
        for (int i = A.length()-1; i >= 0 ; i--)
            A_reverse = A_reverse.concat(String.valueOf(A.charAt(i)));
        System.out.println(A_reverse.equals(A) ? "Yes" : "No");
        sc.close(); // close Scanner object
    }
}
