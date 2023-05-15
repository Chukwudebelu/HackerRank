import java.util.Scanner;

public class Solution {
    static boolean isAnagram(String a, String b) {
        final int m, n;
        m = a.length();
        n = b.length();
        
        // Check strings have same # of characters
        if (m != n) {
            return false; // Not Anagrams
        } else {
            int flag = 0;
            
            for (int i = 0; i < a.length(); i++) {
                char chr = a.charAt(i);
              
                // 1st String
                int count1 = 0;
                for (int j = 0; j < a.length(); j++) {
                    if ((a.charAt(j)+"").equals((chr+"").toUpperCase()) | (a.charAt(j)+"").equals((""+chr).toLowerCase())) {
                        count1++;
                    }
                }
              
                // 2nd String
                int count2 = 0;
                for (int k = 0; k < b.length(); k++) {
                    if ((b.charAt(k)+"").equals((chr+"").toUpperCase()) | (b.charAt(k)+"").equals((""+chr).toLowerCase())) {
                        count2++;
                    }
                }
          
                if (count1 == count2) {
                    flag++;
                    continue;
                } else {
                    break;
                }
            } // for-loop
            if (flag == m) {
                return true;
            } else {
                return false;
            }
        } // if-else
    } //isAnagram

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}
