//!/bin/java
import java.util.*;
import java.text.*;

public class Solution {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    double payment = scanner.nextDouble();
    scanner.close();

    // Get the currency number formats for the Locales
    String us = NumberFormat.getCurrencyInstance(Locale.US).format(payment);
    String india = NumberFormat.getCurrencyInstance(new Locale("en","IN")).format(payment); // new Locale created for India
    String china = NumberFormat.getCurrencyInstance(Locale.CHINA).format(payment);
    String france = NumberFormat.getCurrencyInstance(Locale.FRANCE).format(payment);

    System.out.printf("US: %s\n", us);
    System.out.printf("India: %s\n", india);
    System.out.printf("China: %s\n", china);
    System.out.printf("France: %s", france);

    // Close Scanner Object
    scanner.close();
  }
}
