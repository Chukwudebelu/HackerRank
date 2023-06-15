//!/bin/java
import java.util.*;

public class Solution {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    // Read in the initial # of elements
    int N = scanner.nextInt();
    List<Integer> number_list = new ArrayList<>(N);

    for (int i = 0; i < N; i++) {
      number_list.add(scanner.nextInt());
    }

    // Read in the number of queries
    int Q = scanner.nextInt();

    for (int j = 0; j < Q; j++) {
      String query_type = scanner.next();

      if (query_type.equals("Insert")) {
        int index = scanner.nextInt();
        int element = scanner.nextInt();
        number_list.add(index, element);
      } else if (query_type.equals("Delete")) {
        int index = scanner.nextInt();
        number_list.remove(index);
      }
    }
    // Print the final list
    for (int E : number_list) System.out.print(E + " ");

    // Close Scanner object
    scanner.close();
  }
}
