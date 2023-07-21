//!/bin/java
import java.util.*;

class MyCalculator {
  /* Create the method long power(int, int) here. */
  public static long power (int n, int p) throws Exception {
    if (n < 0 || p < 0) {
      throw new Exception("n or p should not be negative.");
    } else if (n == 0 && p == 0) {
      throw new Exception("n and p should not be zero.");
    }
    
    long n_2_power_p = (long) Math.pow(n, p);
    return n_2_power_p;
  }
}

public class Solution {
  public static final MyCalculator my_calculator = new MyCalculator();
  static final Scanner scan = new Scanner(System.in);
    
  public static void main(String[] args) {
    while (scan.hasNextInt()) {
      int n = scan.nextInt(), p = scan.nextInt();
      
      try {
        long n2p = my_calculator.power(n, p);
        System.out.print(n2p + "\n");
      } catch (Exception e) {
        System.out.print(e.toString() + "\n");
      }
    }
    
    scan.close(); // Close Scanner object
  }
}
