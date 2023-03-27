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
        String s = "";
        for (int i = start; i < end; i++) {
          s += S.charAt(i);
        }
        System.out.printf("%s", s);
    }
}
