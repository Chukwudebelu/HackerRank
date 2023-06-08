//!/bin/java
import java.util.*;

public class Solution 
{
  public static void main(String[] args) 
  {
    Scanner scanner = new Scanner(System.in);
    int ar[][] = new int[6][6];
    int a, b, c, d, e, f, g;
    
    for (int i = 0; i < 6; i++)
    {
      for (int j = 0; j < 6; j++)
      {
        ar[i][j] = scanner.nextInt();
      }
    }
    
    int hourglass_sum;
    int max_sum = -63;  // setting it default by most possible least value
    for (int i = 0; i < 4; i++)
    {
      for (int j = 0; j < 4; j++)
      {
        a = ar[i][j];
        b = ar[i][j+1];
        c = ar[i][j+2];
        d = ar[i+1][j+1];
        e = ar[i+2][j];
        f = ar[i+2][j+1];
        g = ar[i+2][j+2];
        hourglass_sum = a + b + c + d + e + f + g;
        max_sum = Math.max(hourglass_sum, max_sum);
      }
    }
    System.out.print(max_sum + "\n");
    scanner.close(); // Close Scanner object
  }
}
