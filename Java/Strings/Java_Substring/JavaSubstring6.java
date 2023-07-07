//!/bin/java
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        // System.out.println(in.next().substring(in.nextInt(), in.nextInt()));
        char[] s = in.next().toCharArray();
        int a = in.nextInt(), b = in.nextInt();
        for (int i = a; i < b; i++)
          System.out.print(s[i]);
        in.close();
    }
}
