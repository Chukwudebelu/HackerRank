import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
  static int B;
  static int H;
  static boolean flag;

  static {
    Scanner scan = new Scanner(System.in);
    B = scan.nextInt();
    H = scan.nextInt();
    scan.close();
    flag = B > 0 && H > 0;
    
    if (!flag) {
      System.out.print("java.lang.Exception: Breadth and height must be positive");
    }
  }

public static void main(String[] args){
		if (flag) {
			int area = B * H;
			System.out.print(area);
		}
	}//end of main
}//end of class
