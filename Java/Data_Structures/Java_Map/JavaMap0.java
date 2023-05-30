//!/bin/java
// Complete this code or write your own from scratch
import java.util.*;

class Solution {
	public static void main(String []args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		in.nextLine();
    
    // Create a HashMap object - {String=Integer} key/value pairs
    HashMap<String, Integer> phonebook = new HashMap<String, Integer>();
    
    // Insert the username/phone pairs into HashMap
		for (int i = 0; i < n; i++) {
			String name = in.nextLine();
			int phone = in.nextInt();
      phonebook.put(name, phone);
			in.nextLine();
		}
    
		while (in.hasNext()) {
			String s = in.nextLine();
      if (phonebook.get(s) != null) {
        System.out.println(s + "=" + phonebook.get(s));
      } else {
         System.out.println("Not found");
      }
		}
    
    // Close Scanner object
    in.close();
	}
}
