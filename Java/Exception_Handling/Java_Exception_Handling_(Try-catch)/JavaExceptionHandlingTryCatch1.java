import java.lang.ArithmeticException;
import java.util.InputMismatchException;

class Solution {
  public static void main(String[] args) {
    // Enter your code here.
    // Read input from STDIN.
    // Print output to STDOUT.
    // Your class should be named Solution.
    java.util.Scanner s = new java.util.Scanner(System.in);
        
    try {
      int x = s.nextInt();
      int y = s.nextInt();
      System.out.println(x / y);
    } catch (InputMismatchException ie) {
      ie = new InputMismatchException();
      System.out.println(ie);
    } catch (ArithmeticException ae) {
      ae = new ArithmeticException("/ by zero");
      System.out.println(ae);
    } catch (Exception e) {
      System.out.println(e.toString());
    }
    s.close(); // Close Scanner object
  }
}
