import java.math.BigDecimal;
import java.util.*;

class Solution {
    public static void main(String[] args) {
        // Input
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String[] s = new String[n+2];
        for (int i = 0; i < n; i++) {
            s[i] = sc.next();
        }
      	sc.close();

        // Use BigDecimal class to sort the String #s
        // Then, print the actual string representation (i.e. if '.1' print, not '0.1')
        int len = s.length-2;
        
        for (int j = 0; j < len-1; ++j) {
            for (int k = j+1; k < len; ++k) {
              	BigDecimal num1 = new BigDecimal(s[j]);
            	BigDecimal num2 = new BigDecimal(s[k]);
            
				if (num2.compareTo(num1) == 1) { // num2 > num1
				  String temp = s[k];
				  s[k] = s[j];
				  s[j] = temp;              
				} 
          	}
        }
        
        // Output
        for (int i = 0; i < n; i++) {
            System.out.println(s[i]);
        }
    }
}
