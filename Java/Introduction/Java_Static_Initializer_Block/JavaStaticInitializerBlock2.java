import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
  static Scanner scan = new Scanner(System.in);
  static int B, H;
  static boolean flag;
  static {
    B = scan.nextInt();
    H = scan.nextInt();
    scan.close();
    flag = !(B <= 0 || H <= 0);
    
    if (!flag) System.out.print("java.lang.Exception: Breadth and height must be positive");
  } // end of Static Initialization Block

public static void main(String[] args){
		if (flag) {
			int area = B * H;
			System.out.print(area);
		}
	} //end of main
} //end of class

