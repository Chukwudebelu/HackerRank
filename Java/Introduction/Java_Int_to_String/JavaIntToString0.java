import java.util.*;
import java.security.*;
public class Solution {
 public static void main(String[] args) {

  DoNotTerminate.forbidExit();

  try {
   Scanner in = new Scanner(System.in);
   int n = in .nextInt();
   in.close();
   // String s = ???; Complete this line below
   // Write your code here
   String s = "";   
    if (n >= -100 && n <= 100) {
        if (n > 0) {
            while (n > 0) {
                s = (n % 10) + s;
                n = (int) n / 10;
            }
        } else if (n < 0) {
            n *= -1;
            while (n > 0) {
                s = (n % 10) + s;
                n = (int) n /10;
            }
            s = "-" + s; // Append minus sign
        } else {
            s = "0"; // trivial case, iff n = 0
        }
    }
  
   if (n == Integer.parseInt(s)) {
    System.out.println("Good job");
   } else {
    System.out.println("Wrong answer.");
   }
  } catch (DoNotTerminate.ExitTrappedException e) {
   System.out.println("Unsuccessful Termination!!");
  }
 }
}

//The following class will prevent you from terminating the code using exit(0)!
class DoNotTerminate {

 public static class ExitTrappedException extends SecurityException {

  private static final long serialVersionUID = 1;
 }

 public static void forbidExit() {
  final SecurityManager securityManager = new SecurityManager() {
   @Override
   public void checkPermission(Permission permission) {
    if (permission.getName().contains("exitVM")) {
     throw new ExitTrappedException();
    }
   }
  };
  System.setSecurityManager(securityManager);
 }
}
