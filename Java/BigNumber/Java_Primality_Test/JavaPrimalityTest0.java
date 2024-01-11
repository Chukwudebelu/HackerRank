//#!/bin/java7
import java.io.*;
import java.math.*;

public class Solution {
  public static void main(String[] args) throws IOException {
    BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

    String n = bufferedReader.readLine();
    bufferedReader.close(); // Close BufferedReader object
        
    // Create a BigInteger object (# of digits <= 100)
    BigInteger num = new BigInteger(n);
        
    System.out.println((num.isProbablePrime(50)) ? "prime" : "not prime");
  }
}
