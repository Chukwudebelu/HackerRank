import java.util.*;

public class Solution {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    int M = sc.nextInt();
    BitSet B1 = new BitSet(N);
    BitSet B2 = new BitSet(N);
    
    for (int i = 0; i < M; i++) {
      String op = sc.next();
      int p1 = sc.nextInt();
      int p2 = sc.nextInt();
      if (op.equals("AND")) {
        if (p1 == 1) {B1.and(B2);}
        else {B2.and(B1);}
      }
      else if (op.equals("OR")) {
        if (p1 == 1) {B1.or(B2);}
        else {B2.or(B1);}
      }
      else if (op.equals("FLIP")) {
        if (p1 == 1) {B1.flip(p2);}
        else {B2.flip(p2);}
      }
      else if (op.equals("SET")) {
        if (p1 == 1) {B1.set(p2);} 
        else {B2.set(p2);}
      }
      else if (op.equals("XOR")) {
        if (p1 == 1) {B1.xor(B2);}
        else {B2.xor(B1);}
      }
      System.out.println(B1.cardinality() + " " + B2.cardinality());
    }
    // Close Scanner object
    sc.close();
  }
}
