//!/bin/java
import java.util.*;

public class Solution {
    public static void main(String[] args) {        
        Scanner scan = new Scanner(System.in);
        
        for (int i = 1; scan.hasNextLine() == true; i++) {
            String msg = scan.nextLine();
            System.out.println(i + " " + msg);
        }

        // Close Scanner Object
        scan.close();
    }
}
