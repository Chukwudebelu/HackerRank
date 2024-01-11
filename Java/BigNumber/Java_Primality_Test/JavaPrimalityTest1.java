import java.math.BigInteger;

public class Solution {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        BigInteger bigNum = new BigInteger(sc.next());
        
        if (bigNum.isProbablePrime(1) == true)
            System.out.print("prime\n");
        else
            System.out.print("not prime\n");
            
        sc.close(); // Close Scanner object
    }
}
