import java.io.*;
import java.util.*;
import java.math.BigInteger;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scan = new Scanner(System.in);
        String aStr = scan.nextLine(); // Read the 1st # as a string
        String bStr = scan.nextLine(); // Read the 2nd # as a string
        BigInteger a = new BigInteger(aStr);
        BigInteger b = new BigInteger(bStr);
        scan.close(); // close Scanner object
        
        System.out.printf("%d\n%d", a.add(b), a.multiply(b));
    }
}
