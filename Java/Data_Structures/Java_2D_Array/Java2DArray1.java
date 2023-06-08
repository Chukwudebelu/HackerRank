//!/bin/java
import java.util.*;

public class Solution {
    public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
      int n = 6; // array dimension
      int h_top, h_mid, h_bot; // hourglass level sums
      
      // Initialize a 6 x 6 2D array
      int[][] arr = new int[n][n];
      
      for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
          arr[i][j] = scan.nextInt();
        }
      }
      // Hold the smallest value possible
      int max_val = Integer.MIN_VALUE;
      
      for(int i = 0; i < n-2; i++) {
        for(int j = 0; j < n-2; j++) {
          h_top = arr[i][j] + arr[i][j+1] + arr[i][j+2];
          h_mid = arr[i+1][j+1];
          h_bot = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2];
          
          if (h_top + h_mid + h_bot > max_val) 
            max_val = h_top + h_mid + h_bot;
        }
      }
      // Display result
      System.out.printf("%d", max_val);
      
      // Close scanner object
      scan.close();
    }
}
