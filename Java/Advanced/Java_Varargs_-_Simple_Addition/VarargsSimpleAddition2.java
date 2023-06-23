//!/bin/java
// Java7
import java.io.*;
import java.lang.reflect.*;
import java.util.*;

class Add {
    public static void add(int a, int b) {
        System.out.println(a + "+" + b + "=" + (a+b));
    }
    public static void add(int a, int b, int c) {
        System.out.println(a + "+" + b + "+" + c + "=" + (a+b+c));
    }
    public static void add(int a, int b, int c, int d, int e) {
        System.out.println(a + "+" + b + "+" + c + "+" + d + "+" + e + "=" + (a+b+c+d+e));
    }
    public static void add(int a, int b, int c, int d, int e, int f) {
        System.out.println(a + "+" + b + "+" + c + "+" + d + "+" + e + "+" + f + "=" + (a+b+c+d+e+f));
    }
}

public class Solution {
    public static void main(String[] args) {
        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            int n1 = Integer.parseInt(br.readLine());
            int n2 = Integer.parseInt(br.readLine());
            int n3 = Integer.parseInt(br.readLine());
            int n4 = Integer.parseInt(br.readLine());
            int n5 = Integer.parseInt(br.readLine());
            int n6 = Integer.parseInt(br.readLine());
            Add ob = new Add();
            
            ob.add(n1,n2);
            ob.add(n1,n2,n3);
            ob.add(n1,n2,n3,n4,n5);	
            ob.add(n1,n2,n3,n4,n5,n6);
            
            Method[] methods = Add.class.getDeclaredMethods();
            Set<String> set = new HashSet<>();
            boolean overload = false;
            for (int i = 0; i < methods.length; i++) {
                if (set.contains(methods[i].getName())) {
                    overload = true;
                    break;
                }
                set.add(methods[i].getName());
            }
            if (overload) {
				throw new Exception("Overloading not allowed");
            }
        } catch(Exception e) {
            e.printStackTrace();
        }
    }
}
