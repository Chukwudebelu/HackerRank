//!/bin/java
import java.util.*;

public class Solution {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int T = scanner.nextInt();
    String [] pair_left = new String[T];
    String [] pair_right = new String[T];
    
    for (int i = 0; i < T; i++) {
      pair_left[i] = scanner.next();
      pair_right[i] = scanner.next();
    }

    // Create a HashSet object
    HashSet<String> pairs = new HashSet<String>();
    int count = 0;
    
    // Add the pair of strings to the HashSet
    for (int j = 0; j < T; j++) {
      String pair = "(" + pair_left[j] + ", " + pair_right[j] + ")";
      if (!pairs.contains(pair)) {
        count++;
      }
      pairs.add(pair);
      System.out.println(count);
    }
    
    // Close the Scanner object
    scanner.close();
  }
}
