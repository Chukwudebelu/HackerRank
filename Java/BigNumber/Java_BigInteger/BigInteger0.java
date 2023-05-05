import java.io.*;
import java.util.*;
import java.math.BigInteger;

public class Solution {
    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scan = new Scanner(System.in);
        BigInteger a = scan.nextBigInteger(); // Read the 1st #
        BigInteger b = scan.nextBigInteger(); // Read the 2nd #
        scan.close(); // close Scanner object
        
        System.out.println(a.add(b) + "\n" + a.multiply(b));
    }
}
