import java.util.Scanner;
import java.util.regex.*;

public class Solution {
  public static void main(String[] args) {
    Scanner sc = new Scanner (System.in);
    int cases = Integer.parseInt(sc.nextLine());

    while (cases > 0 && sc.hasNextLine()) {
      String patternRegex = sc.nextLine();
      try {
        Pattern p = Pattern.compile(patternRegex);
        System.out.println("Valid");
      }
      catch (PatternSyntaxException e) {
        System.out.println("Invalid");
      }
      cases--;
    }
    sc.close();
  }
}
