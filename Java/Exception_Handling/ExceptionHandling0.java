//!/bin/java
import java.util.*;

public class Solution {
  public static void main(String[] args) {
  /* Enter your code here. Read input from STDIN.
   * Print output to STDOUT.
   * Your class should be named Solution.
   */
    Scanner scan = new Scanner(System.in);
        
    try {
      int x = scan.nextInt();
      int y = scan.nextInt();
      System.out.println(x / y);
    } catch (InputMismatchException ie) {
      ie = new InputMismatchException();
      System.out.println(ie);
    } catch (Exception e) {
      System.out.println(e);
    }
    scan.close(); // Close Scanner object
  }
}
