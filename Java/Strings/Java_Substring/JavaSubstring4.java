import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String S = in.next();
        int start = in.nextInt();
        int end = in.nextInt();
        System.out.print(stringsub(S, start, end));
    }
    
    static String stringsub(String str, int a, int b) {
      return str.substring(a, b);
    }
}
