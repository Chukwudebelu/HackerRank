import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    static Scanner dimensions = new Scanner(System.in);
    private static byte B = dimensions.nextByte(); // breadth
    private static byte H = dimensions.nextByte(); // height
    static boolean flag = B > 0 && H > 0;
    
    static {
      dimensions.close(); // close Scanner Object
      try {
        if (!flag) {
            throw new Exception("Breadth and height must be positive");
        }
      } catch(Exception e) {
            System.out.println(e);
      }
    } // end Static Initialization Block

public static void main(String[] args){
		if (flag) {
			int area = B * H;
			System.out.print(area);
		}	
	} //end of main
} //end of class

