import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String A = sc.next();
        /* Enter your code here. Print output to STDOUT. */
        char[] c = A.toCharArray();
        int n = A.length();
        int flag = 0;
        for (int i = 0; i < (int) A.length()/2; i++) {
            if (c[i] == c[n-1]) {
                flag++;
                n--;
            }
        }
        if (flag == A.length()/2) System.out.println("Yes");
        else System.out.println("No");
        sc.close(); // close Scanner object
    }
}
