import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
            
        String str=sc.nextLine();
        
        int s=sc.nextInt();
        
        int e=sc.nextInt();
        
        StringBuilder ans=new StringBuilder();
        
        for(int i=s;i<e;i++){ans.append(str.charAt(i));}
        
        System.out.println(ans);
    }
}
