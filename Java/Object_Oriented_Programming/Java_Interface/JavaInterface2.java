//!/bin/java
interface AdvancedArithmetic {int divisor_sum(int n);}

// Write your code here
class MyCalculator implements AdvancedArithmetic {
  public int divisor_sum(int n) {
    float m = n;
    // Sum of all the divisors of the number n
    float divisor_sum = 0.0f;
        
    for (float k = 1f; k <= m; k += 1.0) {
      if ((m % k) == 0f) divisor_sum += k;
    }
    return (int) divisor_sum;
  }
}

class Solution {
  public static void main(String[] args) {
    MyCalculator my_calculator = new MyCalculator();
    System.out.print("I implemented: ");
    ImplementedInterfaceNames(my_calculator);
    java.util.Scanner scanner = new java.util.Scanner(System.in);
    int n = scanner.nextInt();
    System.out.print(my_calculator.divisor_sum(n) + "\n");
    scanner.close(); // Close Scanner Object
  }
  /*
   *  ImplementedInterfaceNames method takes an object and
   *  prints the name of the interfaces it implemented
   */
  static void ImplementedInterfaceNames(Object o) {
    Class[] theInterfaces = o.getClass().getInterfaces();
    for (int i = 0; i < theInterfaces.length; i++){
      String interfaceName = theInterfaces[i].getName();
      System.out.println(interfaceName);
    }
  }
}
