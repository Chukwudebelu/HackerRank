//!/bin/java
// Write your code here
class Adder extends Arithmetic
{
  // No Body!
}

class Arithmetic
{
  public int add(int integer1, int integer2)
  {
    return integer1 + integer2;
  }
}

public class Solution
{
  public static void main(String[] args)
  {
    // Create a new Adder object
    Adder a = new Adder();

    // Print the name of the superclass on a new line
    System.out.println("My superclass is: " + a.getClass().getSuperclass().getName());  

    // Print the result of 3 calls to Adder's `add(int,int)` method as 3 space-separated integers:
    System.out.printf("%d %d %d\n", a.add(10,32), a.add(10,3), a.add(10,10));
  }
}
