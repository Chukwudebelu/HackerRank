//#!/bin/java15
import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) {
        // Write your code here
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int numOfWords = 1;
        
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) >= 'A' && s.charAt(i) <= 'Z') {
                numOfWords++;
            }
        }
        System.out.println(numOfWords);
        
        // Close Scanner object
        scan.close();
    }
}
