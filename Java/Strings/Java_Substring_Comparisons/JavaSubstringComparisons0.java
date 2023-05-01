import java.util.Scanner;

public class Solution {
  public static String getSmallestAndLargest(String s, int k) {
    // Complete the function
    // 'smallest' must be the lexicographically smallest substring of length 'k'
    // 'largest' must be the lexicographically largest substring of length 'k'
    // return smallest + "\n" + largest;
    String smallest;
    String largest;
    // Store the length of the string & # of subtrings
    int len = s.length();
    int m = len-k+1;
    // Create a string array
    String[] sub_string = new String[m];
    // Insert substrings into the array
    for (int i = 0; i < m; i++) sub_string[i] = s.substring(i,i+k);
    
    // Sort the substrings
    for (int i = 0; i < m-1; i++) {
      for (int j = i+1; j < m; j++) {
        if (sub_string[i].compareTo(sub_string[j]) > 0) {
          // Perform swapping
          String small = sub_string[j];
          sub_string[j] = sub_string[i];
          sub_string[i] = small;
        }
      }
    }
    smallest = sub_string[0];
    largest = sub_string[m-1];
    return smallest + "\n" + largest;
  }

