//!/bin/java

public class Solution {
  public static void main(String[] args) {
    java.util.Scanner s = new java.util.Scanner(System.in);
    int n = Integer.parseInt(s.nextLine()); // array length
        
    int A[] = new int[n]; // 1D array
        
    for (int i = 0; i < n; i++) {
      A[i] = s.nextInt(); // A = [#, #, ...]
    }
    s.close(); // Close Scanner object

    int subSum = 0; // Sum of subarray
    int count = 0; // Count negative subarrays
        
    for (int j = 0; j < n; j++) {
      subSum = 0; // reset sum
      for (int k = j; k < n; k++) {
        subSum += A[k];
        if (subSum < 0) count++;
      }
    }
    System.out.printf("%d\n", count);
  }
}
