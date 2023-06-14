import java.io.*;
import java.util.*;

public class Solution {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    int n = scan.nextInt();

    // Create a 2D arraylist collection
    List<List<Integer>> myArray = new ArrayList<>();

    // Loop to store all queried arrays
    for (int i = 0; i < n; i++) {
      // 1D arraylist collection
      List<Integer> nums = new ArrayList<>();

      // Length of each 1D subarraylist
      int len = scan.nextInt();

      for (int j = 0; j < len; j++) {
        nums.add((int) Integer.valueOf(scan.next()));
      }
      // Add array to 2D arraylist
      myArray.add(nums);

      // Remove all items from the 1D arraylist
      nums = new ArrayList<>(0);
    }

    // Run the queries
    int q = scan.nextInt();

    for (int k = 0; k < q; k++) {
      int x = scan.nextInt();
      int y = scan.nextInt();

      try {
        System.out.println(myArray.get(x-1).get(y-1));
      } catch (Exception e) {
        System.out.println("ERROR!");
      }
    }
    // Close Scanner object
    scan.close();        
  }
}
