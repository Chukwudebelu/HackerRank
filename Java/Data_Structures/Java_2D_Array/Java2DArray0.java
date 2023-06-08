//!/bin/java
import java.io.*;
import java.util.*;

public class Solution {
  public static void main(String[] args) throws IOException {
    BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
    // Create a 2D dynamic array for entire matrix
    List<List<Integer>> arr = new ArrayList<>();

    for (int i = 0; i < 6; i++) {
      String[] arrRowTempItems = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");
      // Create a 1D dynamic array for the rows
      List<Integer> arrRowItems = new ArrayList<>();
      
      // Insert #s in each row
      for (int j = 0; j < 6; j++) {
        int arrItem = Integer.parseInt(arrRowTempItems[j]);
        arrRowItems.add(arrItem);
      }
      // Add rows to the 2D array
      arr.add(arrRowItems);
    }
    
    // Close BufferedReader object
    bufferedReader.close();
    
    // Create a 1D array to hold the hourglass sums
    ArrayList<Integer> sums = new ArrayList<Integer>();
    int n = 6-2;
    
    // Iterate to get sums
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++){
        int htop = arr.get(i).get(j) + arr.get(i).get(j+1) + arr.get(i).get(j+2);
        int hmid = arr.get(i+1).get(j+1);
        int hbottom = arr.get(i+2).get(j) + arr.get(i+2).get(j+1) + arr.get(i+2).get(j+2);
        // Append sums to array
        sums.add(htop + hmid + hbottom);
      }
    }
    // Display result
    System.out.println(Collections.max(sums));
  }
}
