//!/bin/java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.Scanner;

class Solution {
  public static void main(String[] args){
    Scanner in = new Scanner(System.in);
    while(in.hasNext()) {
      String IP = in.next();
      System.out.println(IP.matches(new MyRegex().pattern));
    }
    in.close(); // Close Scanner object
  }
}

// Write your code here
class MyRegex {
  /* A.B.C.D
   * 000 - 199 -> [01]?[0123456789][0123456789] or
   * 200 - 249 -> [2][01234][0123456789] or
   * 250 - 255 -> [2][5][012345]
   */
  String A = "([01]?[0123456789][0123456789]?|[2][01234][0123456789]|[2][5][012345])"; // 0 to 255
  String B = A, C = A, D = A;
  final String pattern = A + '.' + B + '.' + C + '.' + D;
}
