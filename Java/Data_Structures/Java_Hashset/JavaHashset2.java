//!/bin/java
import java.util.*;

class Solution
{
    public static void main(String []args)
    {
        Scanner input = new Scanner(System.in);
        int n = Integer.parseInt(input.nextLine());
        
        // Create Hashset object
        Set<String> namePairs = new HashSet<>();
        
        // Add new name pairs and display number of items in Hashset
        for (int i = 0; i < n; i++) 
        {
            String userName = input.nextLine();
            namePairs.add(userName);
            System.out.println(namePairs.size());
        }
        
        // Close Scanner object
        input.close();
    }
}
