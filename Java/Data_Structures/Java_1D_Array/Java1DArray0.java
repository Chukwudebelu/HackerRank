//!/bin/java
import java.util.*;

public class Solution {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    int n = scan.nextInt();
    int[] a = new int[n];
    
    // Use a for loop to insert #s in the array
    for (int j = 0; j < n; j++) {
      a[j] = scan.nextInt();
    }
    scan.close(); // Close Scanner object

    // Prints each sequential element in array a
    for (int i = 0; i < a.length; i++) {
      System.out.println(a[i]);
    }
  }
}
