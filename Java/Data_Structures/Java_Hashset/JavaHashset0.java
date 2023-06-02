//!/bin/java
import java.util.Scanner;
import java.util.HashSet;

public class Solution {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    int T = scan.nextInt();
    String [] pair_left = new String[T];
    String [] pair_right = new String[T];
    
    for (int i = 0; i < T; i++) {
      pair_left[i] = scan.next();
      pair_right[i] = scan.next();
    }

    // Create a HashSet object
    HashSet<String> unique_strings = new HashSet<String>();

    // Add the pair of strings to the HashSet
    for (int j = 0; j < T; j++) {
      unique_strings.add(pair_left[j] + " " + pair_right[j]);
      System.out.println(unique_strings.size());
    }
    
    // Close the Scanner object
    scan.close();
  }
}
