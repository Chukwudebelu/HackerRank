import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int[] arr = new int[n];
        
        // 1-D integer array
        for (int i = 0; i < n; i++) {
            arr[i] = scan.nextInt();
        }
        
        Double count_p, count_n, count_z;
        count_p = count_n = count_z = 0.0;
        
        for (int j = 0; j < arr.length; j++) {
            if (arr[j] > 0) {
                count_p++;
            } else if (arr[j] < 0) {
                count_n++;
            } else {
                count_z++;
            }
        }
        
        System.out.printf("%.6f\n", count_p/n);
        System.out.printf("%.6f\n", count_n/n);
        System.out.printf("%.6f\n", count_z/n);
        
        // Close Scanner object
        scan.close();
    }
}
