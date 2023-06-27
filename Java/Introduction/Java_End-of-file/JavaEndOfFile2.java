//!/bin/java
import java.util.Scanner;

public class Solution {
  public static void main(String[] args) {        
    Scanner s = new Scanner(System.in);
    int l = 0; // line of File
    
    while (s.hasNextLine())
      System.out.println((++l) + " " + s.nextLine());
    
    // Close Scanner Object
    s.close();
  }
}
