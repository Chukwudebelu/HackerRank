import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        int M = sc.nextInt();
        
        BitSet B1 = new BitSet();
        BitSet B2 = new BitSet();
        
        while (sc.hasNextLine()) { // Check for next line
          String operation_set = sc.next(); // Read operation
          int num = sc.nextInt(); // BitSet #: 1 or 2
          int op2 = sc.nextInt(); // 2nd #
          
          if (operation_set.equals("AND")) {
            if (num == 1 && op2 == 2) {
              B1.and(B2);
              System.out.printf("%d %d\n", B1.cardinality(), B2.cardinality());
            } else {
              B2.and(B1);
              System.out.printf("%d %d\n", B1.cardinality(), B2.cardinality());
            }
          } else if (operation_set.equals("SET")) {
            if (num == 1) {
              B1.set(op2, true);
              System.out.printf("%d %d\n", B1.cardinality(), B2.cardinality());
            } else {
              B2.set(op2, true);
              System.out.printf("%d %d\n", B1.cardinality(), B2.cardinality());
            }
          } else if (operation_set.equals("FLIP")) {
            if (num == 1) {
              B1.flip(op2);
              System.out.printf("%d %d\n", B1.cardinality(), B2.cardinality());
            } else {
              B2.flip(op2);
              System.out.printf("%d %d\n", B1.cardinality(), B2.cardinality());
            } 
          } else if (operation_set.equals("OR")) {
            if (num == 1 && op2 == 2) {
              B1.or(B2);
              System.out.printf("%d %d\n", B1.cardinality(), B2.cardinality());
            } else {
              B2.or(B1);
              System.out.printf("%d %d\n", B1.cardinality(), B2.cardinality());
            }
          } else if (operation_set.equals("XOR")) {
            if (num == 1 && op2 == 2) {
              B1.xor(B2);
              System.out.printf("%d %d\n", B1.cardinality(), B2.cardinality());
            } else {
              B2.xor(B1);
              System.out.printf("%d %d\n", B1.cardinality(), B2.cardinality());
            }
          }
        }
        // Close Scanner object
        sc.close();
    }
}
