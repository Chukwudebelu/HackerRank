//!/bin/java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.Scanner;

class Solution {
  public static void main(String[] args){
    Scanner scan = new Scanner(System.in);
    while(scan.hasNext()) {
      String IP = scan.next();
      System.out.println(IP.matches(new MyRegex().pattern));
    }
    scan.close(); // Close Scanner object
  }
}

// Write your code here
class MyRegex {
  String reg = "([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])";
  final String pattern = String.format("%s.%s.%s.%s", reg, reg, reg, reg);
}
