//!/bin/java

abstract class Book {
  String title;
  abstract void setTitle(String s);
  
  String getTitle() {
    return title;
  }
}

/* Write MyBook class here */
class MyBook extends Book {
  void setTitle(String s) {
    super.title = s;
  }
}

public class Main {
  public static void main(String[] args) {
    // Book new_novel = new Book();
    // This line prHMain.java:25: error: Book is abstract;
    // cannot be instantiated
    
    java.util.Scanner s = new java.util.Scanner(System.in);
    String title = s.nextLine();
    MyBook new_novel = new MyBook();
    new_novel.setTitle(title);
    System.out.println("The title is: " + new_novel.getTitle());
 
    // Close Scanner Object
    s.close();	
  }
}
