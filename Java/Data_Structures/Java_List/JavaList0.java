//!/bin/java
import java.util.*;

public class Solution {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    
    // Read in the initial # of elements
    int N = scanner.nextInt();
    List<Integer> number_list = new ArrayList<>(N);
    
    for (int i= 0; i < N; i++) {
      number_list.add(scanner.nextInt());
    }
    
    // Read in the number of queries
    int Q = scanner.nextInt();
    int j = 0; // loop variable
    
    while (j++ < Q) {
      switch (scanner.next()) {
        case "Insert":
          int index = scanner.nextInt();
          int element = scanner.nextInt();
          number_list.add(index, element);
          break;
        case "Delete":
          int i = scanner.nextInt();
          number_list.remove(i);
          break;
      }
    }
    // Print the final list
    number_list.forEach(element -> System.out.print(element + " "));
    
    // Close Scanner object
    scanner.close();
  }
}
