import java.io.*;
import java.util.*;


public class Solution {
    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scanner = new Scanner(System.in);

        System.out.println("================================");
        while (scanner.hasNext()) {
            String str = scanner.next();
            int num = scanner.nextInt();
            System.out.printf("%-15s%03d\n", str, num);
        }
        System.out.println("================================");
        scanner.close();
  }
}
