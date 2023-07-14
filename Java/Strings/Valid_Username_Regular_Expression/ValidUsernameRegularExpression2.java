//!/bin/java
import java.util.*;

class UsernameValidator {
  /*
     Write regular expression here.
  */
  public static final String regularExpression = "^([a-zA-Z][a-zA-Z0-9_]{7,29})$";
}

public class Solution {
  private static final Scanner sc = new Scanner(System.in);
    
  public static void main(String[] args) {
    int numberOfLines = Integer.parseInt(sc.nextLine());
    
    while (numberOfLines-- != 0) {
      String userName = sc.nextLine();

      if (userName.matches(UsernameValidator.regularExpression)) {
        System.out.printf("%s\n","Valid");
      } else {
        System.out.printf("%s\n","Invalid");
      }   
    }
    sc.close(); // Close Scanner object
  }
}
