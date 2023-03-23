public class Solution {
    public static void main(String[] args) {
        String msg = "Hello, World.\nHello, Java.";
        
        for (int i = 0; i < msg.length(); i++) {
            System.out.print(msg.substring(i,i+1));
        }
    }
}
