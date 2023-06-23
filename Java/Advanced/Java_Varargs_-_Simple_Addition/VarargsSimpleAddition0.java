//!/bin/java
// Java15
import java.io.*;
import java.lang.reflect.*;
import java.util.*;

// Write your code here
class Add {
  public String add(int... n) {
    int sum_ = 0;
    String disp = "";
    for (int i: n) {
      sum_ += i;
      disp += (i + "+");
    }
  return disp.substring(0,disp.length()-1) + "=" + sum_;
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
      // Create new Add object
      Add ob = new Add();
      
      // Display results
      System.out.println(ob.add(n1,n2));
      System.out.println(ob.add(n1,n2,n3));
      System.out.println(ob.add(n1,n2,n3,n4,n5));  
      System.out.println(ob.add(n1,n2,n3,n4,n5,n6));
      
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
      // Check for Method Overloading
      if (overload) {
        throw new Exception("Overloading not allowed");
      }
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}
