import java.util.*;
import java.io.*;

class Solution {
  public static void main(String[] args) {
   Scanner scan = new Scanner(System.in);       
   int t = scan.nextInt();

   for (int i = 0; i < t; i++) {

       String in = scan.next();

       try {
           Long n = Long.parseLong(in);

           if (n >= Byte.MIN_VALUE && n <= Byte.MAX_VALUE) {
               System.out.println(in + " can be fitted in:");
               System.out.println("* byte\n* short\n* int\n* long");
           }
           else if (n >= Short.MIN_VALUE && n <= Short.MAX_VALUE) {
               System.out.println(in + " can be fitted in:");
               System.out.println("* short\n* int\n* long");
           }
           else if (n >= Integer.MIN_VALUE && n <= Integer.MAX_VALUE) {
               System.out.println(in + " can be fitted in:");
               System.out.println("* int\n* long");
           }
           else {
               System.out.println(in + " can be fitted in:");
               System.out.println("* long");
           }
       }
       catch (Exception e) {
           System.out.println(in + " can't be fitted anywhere.");
       }
     }
  }
}
