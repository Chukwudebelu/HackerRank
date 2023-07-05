import java.util.*;

public class Solution {

  private static final Scanner scanner = new Scanner(System.in);
  
  public static void main(String[] args) {
      int N = scanner.nextInt();
      System.out.println((N%2==1||(N<=20&&N>=6&&N%2==0))?"Weird":"Not Weird");
  }
}
