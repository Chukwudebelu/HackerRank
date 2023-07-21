//!/bin/java

class MyCalculator {
  /* Create the method long power(int, int) here. */
  public long power (int n, int p) throws Exception {
    if (n < 0 || p < 0) {
      throw new Exception("n or p should not be negative.");
    } else if (n == 0 && p == 0) {
      throw new Exception("n and p should not be zero.");
    }
    
    long n_raised_to_p = 1;
    
    for (int j = 0; j < p; j++)
      n_raised_to_p *= n;
      
    return n_raised_to_p;
  }
}

public class Solution {
  public static final MyCalculator my_calculator = new MyCalculator();
  public static final java.util.Scanner s = new java.util.Scanner(System.in);
    
  public static void main(String[] args) {
    while (s.hasNextInt()) {
      int n = Integer.parseInt(s.next());
      int p = Integer.parseInt(s.next());
            
      try {System.out.printf("%d\n", my_calculator.power(n, p));}
      catch (Exception e) {System.out.printf("%s\n", e.toString());}
    }
    
    s.close(); // Close Scanner object
  }
}
