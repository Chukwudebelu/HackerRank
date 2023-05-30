//!/bin/java
import java.util.*;

public class PhoneBook {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int n = scanner.nextInt();
    scanner.nextLine();

    Map<String, String> phoneBook = new HashMap<>();
    
    // Read phone book entries
    for (int i = 0; i < n; i++) {
      String name = scanner.nextLine();
      String phone = scanner.nextLine();
      phoneBook.put(name, phone);
    }
    
    // Process queries
    while (scanner.hasNextLine()) {
      String name = scanner.nextLine();
      if (phoneBook.containsKey(name)) {
        System.out.printf("%s=%s\n", name, phoneBook.get(name));
      } else {
        System.out.println("Not found");
      }
    }
    
    // Close the Scanner object
    scanner.close();
  }
}
