import java.util.Scanner;
import java.util.regex.*;

public class Solution {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    int testCases = Integer.parseInt(scan.nextLine());
    for (int i = testCases; i > 0; i--) {
      String pattern = scan.nextLine();
      // Check if regex can be compiled
      try {
        Pattern.compile(pattern);
        System.out.println("Valid");
      } catch (Exception e) {
        System.out.println("Invalid");
      }
    }
    scan.close(); // close Scanner Object
  }
}
