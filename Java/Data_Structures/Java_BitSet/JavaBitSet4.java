//!/bin/java
import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        BitSet[] B = new BitSet[] {null, new BitSet(N), new BitSet(N)};
        int M = sc.nextInt();
        
        for (int k = 0; k < M; k++) {
            String cmd = sc.next();
            int k1 = sc.nextInt();
            int k2 = sc.nextInt();
            if (cmd.equals("AND")) {
                B[k1].and(B[k2]);
            } else if (cmd.equals("OR")) {
                B[k1].or(B[k2]);
            } else if (cmd.equals("XOR")) {
                B[k1].xor(B[k2]);
            } else if (cmd.equals("FLIP")) {
                B[k1].flip(k2);
            } else if (cmd.equals("SET")) {
                B[k1].set(k2);
            }
            System.out.println(B[1].cardinality() + " " + B[2].cardinality());
        }
        // Close Scanner Object
        sc.close();
    }
}
