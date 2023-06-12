//!/bin/java

public class Solution {
  public static void main(String[] args) {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
    java.util.Scanner in = new java.util.Scanner(System.in);

    int N = in.nextInt();
    int M = in.nextInt();

    java.util.BitSet B1 = new java.util.BitSet(N);
    java.util.BitSet B2 = new java.util.BitSet(N);

    java.util.BitSet[] bitsets = {B1, B2};

    for (int i= 0; i < M ; i++) {
      String op = in.next();
      int a = in.nextInt();
      int b = in.nextInt();

      switch(String.valueOf(op)){
        case "AND" :{
          bitsets[a-1].and(bitsets[b-1]);
          break;
        }
        case "OR" :{
          bitsets[a-1].or(bitsets[b-1]);
          break;
        }
        case "XOR" :{
          bitsets[a-1].xor(bitsets[b-1]);
          break;
        }
        case "FLIP" :{
          bitsets[a-1].flip(b);
          break;
        }
        case "SET" :{
          bitsets[a-1].set(b);
          break;
        }
      }
      System.out.printf("%d %d\n", B1.cardinality(), B2.cardinality());
    }
    // Close Scanner object
    in.close();
  }
}
