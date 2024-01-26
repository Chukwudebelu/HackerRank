import java.util.*;
import java.io.*;

public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        long sum_ = 0;
        
        for (int i = 1; i <= n; i++) {
            sum_ += scanner.nextLong();
        }
        System.out.print(sum_ + "\n");
        
        // Close Scanner object
        scanner.close();
    }
}
