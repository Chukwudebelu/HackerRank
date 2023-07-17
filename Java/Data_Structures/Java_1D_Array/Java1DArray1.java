//!/bin/java

public class Solution {
  public static void main(String[] args) {
    java.util.Scanner s = new java.util.Scanner(System.in);
    int n = Integer.parseInt(s.next());
    int a[] = new int[n];
    
    // Use a for loop to insert #s in the array
    for (int j = 0; j < n; j++)
      a[j] = Integer.parseInt(s.next());
    
    s.close(); // Close Scanner object

    // Prints each sequential element in array a
    for (int element : a)
      System.out.printf("%d\n", element);
  }
}
