import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
            Scanner scan = new Scanner(System.in);
            System.out.println("================================");
            for (int i = 0; i < 3; i++) {
                String str = scan.next();
                String str_format = String.format("%-15s", str);
                int x = scan.nextInt();
                String x_format = String.format("%03d", x);
                System.out.println(str_format + x_format);
            }
            System.out.println("================================");
            scan.close();
    }
}
