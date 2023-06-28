//!/bin/java

public class Solution {
  public static void main(String[] args) {
    java.util.Scanner sc = new java.util.Scanner(System.in);
    String A = sc.nextLine(), B = sc.nextLine();
    
    System.out.println(A.length() + B.length());
    System.out.println((A.compareTo(B) > 0) ? "Yes" : "No");
    char a = Character.toUpperCase(A.charAt(0));
    char b = Character.toUpperCase(B.charAt(0));
    System.out.printf("%s %s\n", a + A.substring(1), b + B.substring(1));
    
    // Close Scanner object
    sc.close();
  }
}
