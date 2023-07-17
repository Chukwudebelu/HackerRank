import java.util.Scanner;

public class Solution {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = Integer.parseInt(sc.nextLine());
    
    int count = 0;
    while (count <= n) {
      if (count != 0) // Skip 1st line: Denotes array size!
        System.out.print(sc.nextLine() + "\n");
      count++;
    }
    sc.close(); // Close Scanner object
  }
}
