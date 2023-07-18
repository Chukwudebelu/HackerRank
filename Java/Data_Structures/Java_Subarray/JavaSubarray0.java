//!/bin/java
import java.util.*;

public class Solution {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    int n = Integer.parseInt(scan.nextLine()); // array length
        
    int A[] = new int[n]; // 1D array
        
    for (int i = 0; i < n; i++) {
      A[i] = scan.nextInt(); // A = [#, #, ...]
    }
        
    int w = 1; // Initialize width of sliding window
    int count = 0; // Count negative subarrays
        
    while (w <= n) {
      for (int j = 0; j < n-w+1; j++) {
        int[] sub_array = Arrays.copyOfRange(A, j, j+w);
        int sum_ = 0;
            
        for (int e : sub_array) {
          sum_ += e;
        }
        if (sum_ < 0) count++;
      }
      w++;
    }
    System.out.print(count);
        
    scan.close(); // Close Scanner object
  }
}
