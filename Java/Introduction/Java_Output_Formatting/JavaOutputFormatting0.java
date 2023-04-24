import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
            Scanner scan = new Scanner(System.in);
            System.out.println("================================");
      
            for (int i = 0; i < 3; i++) {
                String str = scan.next();
                int x = scan.nextInt();
                System.out.printf("%-15s%03d\n", str, x);
            }
            System.out.println("================================");
            scan.close(); // Close the scanner object;
    }
}
