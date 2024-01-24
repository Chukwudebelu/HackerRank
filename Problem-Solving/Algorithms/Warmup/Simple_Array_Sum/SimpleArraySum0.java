import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int arLength = sc.nextInt();       
        int sum_ = 0;
        
        for (int i = 0; i < arLength; i++) {
            sum_ += sc.nextInt();
        }
        System.out.printf("%d", sum_);
        
        // Close Scanner object
        sc.close();
    }
}
