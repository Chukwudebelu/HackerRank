//!/bin/java

public class Solution {
  public static void main(String[] args) {        
    java.util.Scanner sc = new java.util.Scanner(System.in);
    int line = 1; // 1st line of File
    
    while (sc.hasNextLine()) {
      String message = sc.nextLine(); // line content
      System.out.printf("%d %s\n", line, message);
      line++;
    }
    
    // Close Scanner Object
    sc.close();
  }
}
